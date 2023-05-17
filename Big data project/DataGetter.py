from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.PDBList import PDBList
from Bio.SeqIO import PdbIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import ExPASy
import ensembl_rest
from bioservices import UniProt
from chembl_webresource_client.new_client import new_client
import concurrent.futures
import subprocess
import pandas
import pypdb
import json
import os
import io


def Get_Protein_Properties(pdb_id):
    pdblist_obj = PDBList()
    file_path = pdblist_obj.retrieve_pdb_file(pdb_id, file_format='pdb')
    structure_id = pdb_id
    pdb_parser = PDBParser()
    strucuture = pdb_parser.get_structure(structure_id, file_path)
    name = strucuture.header["name"]
    pdb_id = strucuture.header["idcode"]
    seqrec_iterator = PdbIO.PdbSeqresIterator(file_path)

    for record in seqrec_iterator:
        index_1 = record.dbxrefs[0].find(':') + 1
        uniprot_id = record.dbxrefs[0][index_1:]
        break

    with ExPASy.get_sprot_raw(uniprot_id) as handle:
        seq_record = SeqIO.read(handle, "swiss")

    SeqIO.write(seq_record, f'{pdb_id}.fasta', "fasta")


def Get_Disease_Properties(gene_omim_number=None, disease_omim_number=None):
    if gene_omim_number:
        cwd = os.getcwd()
        file_path = "Gene.json"
        command = f'omim query -s mim_number {gene_omim_number} -F json -o {file_path}'
        gene_data = Run_Omim_Query(command=command, file_path=file_path)
        os.chdir(cwd)

        return Get_Data_From_Gene_Omim_Number(gene_data)

    elif disease_omim_number:
        cwd = os.getcwd()
        file_path = "Disease.json"
        command = f'omim query -s mim_number {disease_omim_number} -F json -o {file_path}'
        disease_data = Run_Omim_Query(command=command, file_path=file_path)
        os.chdir(cwd)
        return Get_Data_From_Disease_Omim_Number(disease_data)


def Get_BioActivity_Properties(uniprot_id):
    targets_api = new_client.target
    compounds_api = new_client.molecule

    targets = targets_api.get(target_components__accession=uniprot_id).only(
        "target_chembl_id", "organism", "pref_name", "target_type"
    )
    targets = pandas.DataFrame.from_records(targets)
    target = targets.iloc[0]
    chembl_id = target.target_chembl_id
    types = ["IC50", "Ki", "GI50", "EC50", "Kd"]
    ids = [chembl_id] * len(types)
    with concurrent.futures.ThreadPoolExecutor() as exe:
        results = exe.map(Get_BioActivities, ids, types)
    activities_values = [value for value in results]

    return types, activities_values


def Get_BioActivities(chembl_id, bioactivity_type):
    bioactivities_api = new_client.activity
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


def Run_Omim_Query(command, file_path):
    os.chdir("C:\\Users\\hkame")
    _ = subprocess.run(command, shell=True, capture_output=True)
    with open(file_path, 'r') as infile:
        json_data = json.load(infile)[0]

    return json_data


def Get_Data_From_Gene_Omim_Number(json_data):
    ensemble_id = json_data["ensembl_gene_id"]

    diseaes_info = {}
    for disease in json_data["geneMap"]:
        if disease["Inheritance"] == "":
            diseaes_info[disease["Phenotype"]] = "No Inheritance"
        else:
            diseaes_info[disease["Phenotype"]] = disease["Inheritance"]

    gene_seq = ensembl_rest.sequence_id(ensemble_id)["seq"]

    gene_symbol = json_data["hgnc_gene_symbol"]

    service = UniProt()
    query = f'{gene_symbol} AND HUMAN'
    result = service.search(query)
    result_df = pandas.read_table(io.StringIO(result))
    uniprot_id = result_df["Entry"][0]
    fasta = service.get_fasta(uniprot_id)
    protein_seq = SeqIO.read(io.StringIO(fasta), 'fasta')
    pdb_ids = pypdb.Query(uniprot_id).search()

    return diseaes_info, gene_seq, str(protein_seq.seq), pdb_ids


def Get_Data_From_Disease_Omim_Number(json_data):
    diseases = {}
    for disease in json_data["phenotypeMap"]:
        if "susceptibility to" in disease["Phenotype"]:
            continue
        cwd = os.getcwd()
        file_path = "results.json"
        command = f'omim query -s mim_number {disease["Gene/Locus MIM number"]} -F json -o {file_path}'
        gene_data = Run_Omim_Query(command, file_path)
        _, gene_seq, prot_seq, pdb_ids = Get_Data_From_Gene_Omim_Number(gene_data)

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
