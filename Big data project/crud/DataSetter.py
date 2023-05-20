"""
    The DataSetter.py script contains a set of functions each of them is responsible for populating each collection properties 
    wih the data returned from the functions from the DataGetter.py and each returns an object of the collection... 
"""
from DataGetter import *
from Diseasome import *

##Pre-conditions: the wanted PDB id as a string and the Protein collection object for handling Protein collection in mongo...
##Post-condtions: it will return an object of type Protein populated with data returned from the Get_Protein_Properties function...
def Set_Protein_Properties(pdb_id, protein_collection):
    protein_obj = Protein(protein_collection)

    try:
        name, structure, fasta_format = Get_Protein_Properties(pdb_id)
        protein_obj.id = pdb_id
        protein_obj.name = name
        protein_obj.structure = structure
        protein_obj.fasta = fasta_format

        return protein_obj
    
    except:
        if Get_Protein_Properties(pdb_id) == -1:
            print("An error occurred during downloading the PDB file...")
            return
        elif Get_Protein_Properties(pdb_id) == -2:
            print("An error occurred during downloading the Uniprot record...")
            return
    
##Pre-conditions: the wanted Uniprot id as a string and the BioActivity collection object for handling BioActivity collection in mongo...
##Post-condtions: it will return an object of type BioActivity populated with data returned from the Get_BioActivity_Properties function...
def Set_BioActivity_Properties(uniprot_id, bioactivity_coll):
    bioactivity_obj = BioActivity(bioactivity_coll)
    try:
        types, vals, ligand_id = Get_BioActivity_Properties(uniprot_id)
        bioactivity_obj.ic50 = vals[types.index("IC50")]
        bioactivity_obj.ec50 = vals[types.index("EC50")]
        bioactivity_obj.gi50 = vals[types.index("GI50")]
        bioactivity_obj.ki = vals[types.index("Ki")]
        bioactivity_obj.kd = vals[types.index("Kd")]
        bioactivity_obj.ligand_fk = ligand_id
        bioactivity_obj.id = uniprot_id
        
        return bioactivity_obj

    except:
        if Get_BioActivity_Properties(uniprot_id) == -1:
            print("An error occurred during downloading the targets records...")
            return
        
##Pre-conditions: the wanted omim number as a string and the Disease collection object for handling Disease collection in mongo...
##Post-condtions: it will return an object of type Disease populated with data returned from the Get_Disease_Properties function...
def Set_Disease_Properties(disease_collection, omim_disease_name, gene_omim_number=None, disease_omim_number=None):
    disease_obj = Disease(disease_collection)

    try:
        if gene_omim_number:
            disease_info, gene_seq, protein_seq, pdb_ids = Get_Disease_Properties(gene_omim_number=gene_omim_number)
            disease_obj.name = omim_disease_name
            disease_obj.type = disease_info.get(omim_disease_name, "")
            disease_obj.gene_seq = gene_seq
            disease_obj.protein_seq = protein_seq
            disease_obj.pdb_fk = pdb_ids

            return disease_obj
    
    except:
        if Get_Disease_Properties(gene_omim_number=gene_omim_number) == -1:
            print("An error occurred during fetching the gene sequence from Ensemble")
            return
        
        elif Get_Disease_Properties(gene_omim_number=gene_omim_number) == -2:
            print("An error occurred during fetching the Uniport id")
            return
        
        elif Get_Disease_Properties(gene_omim_number=gene_omim_number) == -3:
            print("An error occurred during fetching the protein sequence and PDB ids")
            return
        

##Pre-conditions: the wanted PDB id as a string and the Dock collection object for handling Dock collection in mongo...
##Post-condtions: it will return an object of type Dock populated with data returned from the Get_BioActivity_Properties function...
def Set_Dock_Properties(pdb_id, dock_collection):
    dock_obj = Dock(dock_collection)

    try:
        dock_vals = Get_Dock_Properties(pdb_id)
        dock_obj.num_of_itermolecular_contacts = int(dock_vals[0])
        dock_obj.num_of_charged_charged_contacts = int(dock_vals[1])
        dock_obj.num_of_charged_polar_contacts = int(dock_vals[2])
        dock_obj.num_of_charged_apolar_contacts = int(dock_vals[3])
        dock_obj.num_of_polar_polar_contacts = int(dock_vals[4])
        dock_obj.num_of_apolar_polar_contacts = int(dock_vals[5])
        dock_obj.num_of_apolar_apolar_contacts = int(dock_vals[6])
        dock_obj.apolar_nis_residues_percentage = dock_vals[7]
        dock_obj.charged_nis_residues_percentage = dock_vals[8]
        dock_obj.binding_affinity = dock_vals[9]
        dock_obj.dissociation_constant = dock_vals[10]

        return dock_obj
    
    except:
        if Get_Dock_Properties(pdb_id) == -1:
            print("An error occurred during downloading the PDB file...")
            return
        
        elif Get_Dock_Properties(pdb_id) == -2:
            print("An error occurred during getting docking properties...")
            return

##Pre-conditions: the wanted chembl id as a string and the Ligand collection object for handling Ligand collection in mongo...
##Post-condtions: it will return an object of type Ligand populated with data returned from the Get_Ligand_Properties function...
def Set_Ligand_Properties(ligand_id, ligand_collection):
    ligand_obj = Ligand(ligand_collection)

    ligand_properties = Get_Ligand_Properties(ligand_id)
    if ligand_properties == 0:
        print("Nothing has been returned")
        return
    elif ligand_properties == -1:
        print('Error: Could not establish connection with the ChEMBL Web Services.')
        return
    else:
        ligand_obj.id = ligand_id
        ligand_obj.name = ligand_properties["common_name"]
        ligand_obj.solubility = ligand_properties["solubility"]
        ligand_obj.logp = ligand_properties["logp"]
        ligand_obj.molecular_weight = ligand_properties["mol_weight"]
        ligand_obj.iupac = ligand_properties["iupac_name"]
        ligand_obj.structure = ligand_properties["structure"]
        ligand_obj.drug_score = ligand_properties["drug_score"]
        ligand_obj.drug_like = ligand_properties["drug_like"]
        ligand_obj.smile_format = ligand_properties["smiles"]
        ligand_obj.molecular_formula = ligand_properties["mol_formula"]

        return ligand_obj
