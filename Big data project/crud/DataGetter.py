"""
    The DataGetter.py script contains a set of functions each of them is responsible for getting each collection properties data. 
"""
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.PDBList import PDBList
from Bio.SeqIO import PdbIO
from Bio import SeqIO
from Bio import ExPASy
import ensembl_rest
from bioservices import UniProt
from chembl_webresource_client.new_client import new_client
import concurrent.futures
import subprocess
import pickle
import pandas
import pypdb
import json
import os
import io
from Diseasome import *


##Pre-conditions: an existed PDB id must be passed to the function as a string value without any spaces...
##Post-conitions: if no errors happend the function will return: name of the protein, structure of the protein in binary format,
# the fasta format of the protein sequence as a string value, otherwise it will return -1 if error occurred while fetching
# the PDB file or -2 while fetching the Uniprot record...
def Get_Protein_Properties(pdb_id):
    pdblist_obj = PDBList()  # This object deals with the PDB server...
    try:
        # The next function downloads the requeste PDB file and returns its path in your device...
        file_path = pdblist_obj.retrieve_pdb_file(pdb_id, file_format='pdb')
    except:
        return -1
    structure_id = pdb_id
    pdb_parser = PDBParser()  # This object handles the PDB files...
    structure = pdb_parser.get_structure(structure_id, file_path)  # Returns the protein structure and its metadata...
    name = structure.header["name"]  # Protein name
    seqrec_iterator = PdbIO.PdbSeqresIterator(
        file_path)  # This object returns SeqRecord objects for each chain in a PDB file...
    # Getting the uniprot id from the PDB file...
    for record in seqrec_iterator:
        index_1 = record.dbxrefs[0].find(':') + 1
        uniprot_id = record.dbxrefs[0][index_1:]
        break
    try:
        # Getting the protein sequence from the uniport...
        with ExPASy.get_sprot_raw(uniprot_id) as handle:
            seq_record = SeqIO.read(handle, "swiss")
    except:
        return -2

    # Writing the protein sequence in file with fasta format
    # Then read it and convert it to a string...
    SeqIO.write(seq_record, f'{pdb_id}.fasta', "fasta")

    fasta_format = ""
    with open(f'{pdb_id}.fasta', 'r') as infile:
        for line in infile:
            fasta_format += line.strip()

    pickled_structure = pickle.dumps(
        structure)  # Converting the PDB strucutre into binary format to enable storing it into Mongodb...

    os.remove(f'{pdb_id}.fasta')  # Removing the fasta file...

    return name, pickled_structure, fasta_format


##Pre-conditions: an existed Uniprot id must be passed to the function as a string value without any spaces
# and a list of the activity types you want to extract, bydefault they are "IC50", "Ki", "GI50", "EC50", "Kd"...
##Post-conditions: without errors, the function will return the list of the provided types "you can igonre it", the list of the
# returned values , and the target chembl id, else -1 will be returned indicating an error happend while fetching target data...
def Get_BioActivity_Properties(uniprot_id, types=["IC50", "Ki", "GI50", "EC50", "Kd"]):
    targets_api = new_client.target  # This object deals with getting target data from chembl...

    try:
        # Getting all the targets related with the provided Uniprot id...
        targets = targets_api.get(target_components__accession=uniprot_id).only(
            "target_chembl_id", "organism", "pref_name", "target_type"
        )
        # Converting the fetched data into pandas DataFrame...
        targets = pandas.DataFrame.from_records(targets)
    except:
        return -1

    # Getting the target chembl id for which we will get the activity values, the target well be the first record as
    # it's a single protein...
    target = targets.iloc[0]
    chembl_id = target.target_chembl_id
    # Getting the value for each bioActivity type in the provided list...
    activities_values = []
    for typ in types:
        activities_values.append(Get_BioActivities(chembl_id, typ))

    return types, activities_values, chembl_id


##Pre-conditions: it takes the target chembl id for which we will get the activity values, and the activity type i.e, IC50, Ki, etc.
##Post-conditions: it returns 0.0 if no value found, else it will the data fetched...
def Get_BioActivities(chembl_id, bioactivity_type):
    bioactivities_api = new_client.activity  # This object deals with getting activity data from chembl...
    # Getting the activity data related with the provided target chembl id...
    bioactivities = bioactivities_api.filter(target_chembl_id=chembl_id, type=bioactivity_type, relation="=",
                                             assay_type="B").only(
        "activity_id",
        "assay_chembl_id",
        "assay_description",
        "assay_type",
        "molecule_chembl_id",
        "type",
        "standard_units",
        "relation",
        "standard_value",
        "target_chembl_id",
        "target_organism",

    )

    if not bioactivities:
        return 0.0
    else:
        return bioactivities[0]["standard_value"]


##Pre-conditions: a gene of disease omim number is porvided, else nothing will be returned..
##Post-conditions: if a gene omim number is porvided then the function returns the value returned from the Get_Data_From_Gene_Omim_Number
# if the disease omim number then the function returns results returned from Get_Data_From_Disease_Omim_Number...
def Get_Disease_Properties(gene_omim_number=None, disease_omim_number=None):
    if gene_omim_number:
        cwd = os.getcwd()
        file_path = "Gene.json"
        command = f'omim query -s mim_number {gene_omim_number} -F json -o {file_path}'
        gene_data = Run_Omim_Query(command=command, file_path=file_path)
        if gene_data == -1:
            return -1

        os.chdir(cwd)

        return Get_Data_From_Gene_Omim_Number(gene_data)

    elif disease_omim_number:
        cwd = os.getcwd()
        file_path = "Disease.json"
        command = f'omim query -s mim_number {disease_omim_number} -F json -o {file_path}'
        disease_data = Run_Omim_Query(command=command, file_path=file_path)
        if disease_data == -1:
            return -1

        os.chdir(cwd)
        return Get_Data_From_Disease_Omim_Number(disease_data)


##Pre-conditions: an omim query command , and the file path in which the query results will be stored must be passed,
# and the file is a json file...
##Post-conditions: if no errors happend while runing the omim query the json_data with query results will be returned, otherwise
# -1 will be returned 
def Run_Omim_Query(command, file_path):
    os.chdir("C:\\Users\\hkame")  # changing the directory to the one contains the omim tool...
    process = subprocess.run(command, shell=True, capture_output=True)
    if process != 0:
        return -1

    with open(file_path, 'r') as infile:
        json_data = json.load(infile)[0]

    return json_data


##Pre-conditions: a gene json data returned from omim query is provided, else not valid results will be returned and maybe errors...
##Post-conditions: the function will return a dictionary contains each disease related the gene with disease name as a key and,
# disease type as a value, the gene sequence, the protein sequence, and the PDB ids, otherwise, -1 if error happened in fetching
# the gene sequence, -2 if errors hapened in fetching uniport id, -3 if errors happened in fetching PDB ids and protein sequence... 
def Get_Data_From_Gene_Omim_Number(json_data):
    ensemble_id = json_data["ensembl_gene_id"]  # Get ensemble id from which we will get the gene sequence...

    # construct a dictionary contains the disease name as a key and the inheritance type as a value, the dictionary contains 
    # all diseases related to the gene...
    diseaes_info = {}
    for disease in json_data["geneMap"]:
        if disease["Inheritance"] == "":
            diseaes_info[disease["Phenotype"]] = "No Inheritance"
        else:
            diseaes_info[disease["Phenotype"]] = disease["Inheritance"]

    try:
        # Fetch the gene sequence from Ensemble... 
        gene_seq = ensembl_rest.sequence_id(ensemble_id)["seq"]
    except:
        return -1

    gene_symbol = json_data[
        "hgnc_gene_symbol"]  # the gene symbol will be used to get Uniprot id related to that gene...

    service = UniProt()  # this object to access Uniprot...
    query = f'{gene_symbol} AND HUMAN'
    try:
        result = service.search(query)  # search and getting the uniprot records
        result_df = pandas.read_table(io.StringIO(result))  # putting the search results into pandas DataFrame
        uniprot_id = result_df["Entry"][0]  # Taking the first entry which is our target...
    except:
        return -2
    try:
        fasta = service.get_fasta(uniprot_id)
        # converting the search result into a SeqRecord object containing the protein sequence...
        protein_seq = SeqIO.read(io.StringIO(fasta), 'fasta')
        pdb_ids = pypdb.Query(uniprot_id).search()  # Getting all the PDB ids related to that Uniprot protein...
    except:
        return -3

    return diseaes_info, gene_seq, str(protein_seq.seq), pdb_ids


##Pre-conditions: a protein json data returned from omim query is provided, else not valid results will be returned and maybe errors...
##Post-conditions: a dictionary has the disease name as a key and each key has a list of dictionart each dictionary contains 
# the gene sequence, protein sequence, PDB ids, and disease type related to the contributing gene, since the same disease may be caused
# by different genes, otherwise, -1 or error values will be returned...
def Get_Data_From_Disease_Omim_Number(json_data):
    diseases = {}  # this dictionary will contain all the data related with that disesae, the disease name is the key, and
    # the values is a list of dictionaries each contains: gene sequence, protein sequence, PDB ids, and disease type
    for disease in json_data["phenotypeMap"]:
        cwd = os.getcwd()
        file_path = "results.json"
        command = f'omim query -s mim_number {disease["Gene/Locus MIM number"]} -F json -o {file_path}'
        gene_data = Run_Omim_Query(command, file_path)
        os.chdir(cwd)
        if gene_data == -1:
            return -1
        try:
            _, gene_seq, prot_seq, pdb_ids = Get_Data_From_Gene_Omim_Number(gene_data)
        except:
            return Get_Data_From_Gene_Omim_Number(gene_data)  # will return -1, -2, or -3...

        # Populating the diseases dictionary...
        if disease["Inheritance"] == "":
            if diseases.get(disease["Phenotype"]):
                values = {
                    "GeneSeq": gene_seq,
                    "ProtSeq": prot_seq,
                    "PdbIds": pdb_ids,
                    "Type": "No Inheritance"
                }
                diseases[disease["Phenotype"]].append(values)
            else:
                diseases[disease["Phenotype"]] = []
                values = {
                    "GeneSeq": gene_seq,
                    "ProtSeq": prot_seq,
                    "PdbIds": pdb_ids,
                    "Type": "No Inheritance"
                }
                diseases[disease["Phenotype"]].append(values)
        else:
            if diseases.get(disease["Phenotype"]):
                values = {
                    "GeneSeq": gene_seq,
                    "ProtSeq": prot_seq,
                    "PdbIds": pdb_ids,
                    "Type": disease["Inheritance"]
                }
                diseases[disease["Phenotype"]].append(values)
            else:
                diseases[disease["Phenotype"]] = []
                values = {
                    "GeneSeq": gene_seq,
                    "ProtSeq": prot_seq,
                    "PdbIds": pdb_ids,
                    "Type": disease["Inheritance"]
                }
                diseases[disease["Phenotype"]].append(values)

    return diseases

    ##Pre-conditions: a PDB id of a complex provided in a string format...
    ##Post-conditions: returns a list contains the dock values: ordered according to their index
    """
        number of intermolecular contacts
        number of charged charged contacts
        number of charged polar contacts
        number of charged apolar contacts
        number of polar polar contacts
        number of apolar polar contacts
        number of apolar apolar contacts
        Apolar NIS residues percentage
        Charged NIS residues percentage
        Binding affinity
        Dissociation constant

    """


# oherwise it will returns -1 if error happened during fetchting the PDB file, or -2 if error happened during calculating
# the properties...
def Get_Dock_Properties(pdb_id):
    cwd = os.getcwd()
    os.chdir("C:\\Users\\hkame\\prodigy")  # changing the directory to the one contains the prodigy tool...

    pdb_file_name = f'{pdb_id}.pdb'
    pdb_file_getter_command = f'curl -o {pdb_file_name} https://files.rcsb.org/download/{pdb_id}.pdb'

    process1 = subprocess.run(pdb_file_getter_command, shell=True, capture_output=True)
    if process1.returncode != 0:
        return -1

    with open("prodigy_output.txt", 'w') as outfile:
        process2 = subprocess.run(f'prodigy {pdb_file_name}', shell=True, text=True, stdout=outfile)
        if process2.returncode != 0:
            return -2

    with open("prodigy_output.txt", 'r') as infile:
        lines = infile.readlines()
        output_values = []
        for line in lines[2:]:
            line = line.strip()
            start_index = line.find(':') + 2
            output_values.append(float(line[start_index:]))

    os.remove(pdb_file_name)
    os.remove("prodigy_output.txt")
    os.chdir(cwd)

    return output_values


##Pre-conditions: the chembl id for the wanted ligand
##Post-conditions: the function returns a dictionary contains: smiles, molecular weight, logp, molecular formula, solubility, iupac name,
# structure, name, lims_id, drug score, drug like, otherwise a 0 will be returned...
def Get_Ligand_Properties(ligand_id):
    try:
        # consedireing the compound is the ligand
        # Retrieve the compound information using the Molecule model
        Ligand = new_client.molecule.get(ligand_id)

        # Define an empty dictionary to store the information
        ligand_entery = {}

        # Check if the compound information was retrieved successfully
        if Ligand is not None:
            # Extract the information you need from the compound object
            ligand_entery['smiles'] = Ligand['molecule_structures']['canonical_smiles']
            ligand_entery['mol_weight'] = Ligand['molecule_properties']['mw_freebase']
            ligand_entery['logp'] = Ligand['molecule_properties']['alogp']
            ligand_entery['mol_formula'] = Ligand['molecule_properties']['full_molformula']
            ligand_entery['solubility'] = Ligand['molecule_properties'].get('alogps_solubility', None)
            ligand_entery['iupac_name'] = Ligand['molecule_properties'].get('iupac_name', None)
            ligand_entery['structure'] = Ligand['molecule_structures']['molfile']
            ligand_entery['common_name'] = Ligand['molecule_synonyms'][0]['synonyms']
            ligand_entery['lims_id'] = Ligand['molecule_properties'].get('lims_id', None)
            ligand_entery['drug_score'] = Ligand['molecule_properties'].get('drug_ro5_violations', None)
            ligand_entery['drug_like'] = Ligand['molecule_properties'].get('drug_likeness', None)
            ligand_entery["structure"] = pickle.dumps(ligand_entery["structure"])
            return ligand_entery

        else:
            print(f'Ligand with ChEMBL ID {ligand_id} not found')
            return 0
    except:
        return -1
