from pymongo import MongoClient
from Bio.PDB.PDBParser import PDBParser
import pickle
import nglview as nv

class crud:

    def __init__(self):
        # Create connection
        MONGODB_URL = "mongodb+srv://Al-Hassan:Bigdata1128@bigdataproject.nhz6c7e.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(MONGODB_URL)
        db = client.Diseasome

        # Collections
        self.Protein_collection = db.Protein
        self.Ligand_collection = db.Ligand
        self.Dock_collection = db.Dock
        self.Disease_collection = db.Disease
        self.BioActivity_collection = db.BioActivity

    # ======================================================================================================================= Bio Activity

    def BioActivity_insert(self, id, ic50, ki, gi50, ec50, kd, ligand_fk):
        bioActivity_to_insert = {
            "id": id,
            "IC50": ic50,
            "Ki": ki,
            "GI50": gi50,
            "EC50": ec50,
            "Kd": kd,
            "Ligand_fk": ligand_fk,
        }
        try:
            insert_res = self.BioActivity_collection.insert_one(bioActivity_to_insert)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    # ======================================================================================================================= Disease
    def Disease_search(self, id, name):
        disease_to_find = {
            "id": id,
            "Name": name
        }
        search_res = self.Disease_collection.find_one(disease_to_find)
        if search_res:
            disease_id = search_res["id"]
            disease_name = search_res["Name"]
            PDB_fk = search_res["PDB_fk"]
            protein_seq = search_res["ProteinSeq"]
            disease_type = search_res["Type"]
            geneSeq = search_res["GeneSeq"]
            gene_locus = search_res["Gene Locus"]
            return disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus
        else:
            return None

    def Disease_insert(self, id, name, pdb_fk, protein_seq, d_type, gene_seq, gene_locus):
        pdb_fk = pdb_fk.split(",")
        disease_to_insert = {
            "id": id,
            "Name": name,
            "PDB_fk": pdb_fk,
            "ProteinSeq": protein_seq,
            "Type": d_type,
            "GeneSeq": gene_seq,
            "Gene Locus": gene_locus,
        }
        try:
            insert_res = self.Disease_collection.insert_one(disease_to_insert)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    # ======================================================================================================================= Dock
    def Dock_insert(self, id, num_of_intermolecular_contacts, num_of_charged_charged_contacts,
                    num_of_charged_polar_contacts, num_of_charged_apolar_contacts, num_of_polar_polar_contacts,
                    num_of_aploar_polar_contacts, num_of_apolar_apolar_contacts, binding_affinity,
                    dissociation_constant,
                    charged_nis_residues_percentage, aploar_nis_residues_percentage, ligand_id, pdb_id):
        dock_to_insert = {
            "id": id,
            "Intermolecular Contacts": num_of_intermolecular_contacts,
            "Charged-Charged_Contacts": num_of_charged_charged_contacts,
            "Charged-Polar-Contacts": num_of_charged_polar_contacts,
            "Charged-Apolar-Contacts": num_of_charged_apolar_contacts,
            "Polar-Polar-Contacts": num_of_polar_polar_contacts,
            "Apolar-Polar-Contacts": num_of_aploar_polar_contacts,
            "Apolar-Apolar-Contacts": num_of_apolar_apolar_contacts,
            "Dissociation Constant": dissociation_constant,
            "Binding Affinity": binding_affinity,
            "Charged NIS Residues Percentage": charged_nis_residues_percentage,
            "Apolar NIS Residues Percentage": aploar_nis_residues_percentage,
            "Ligand_id": ligand_id,
            "PDB_id": pdb_id,
        }
        try:
            insert_res = self.Dock_collection.insert_one(dock_to_insert)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    # ======================================================================================================================= Ligand
    def Ligand_insert(self, id, Name, Solubility, LogP, MolecularWeight, IUPAC, Structure, DrugScore, DrugLike,
                      SmileFormat, MolecularFormula):
        pdb_parser = PDBParser()
        strcuture = pdb_parser.get_structure(id, Structure)
        pickled_structure = pickle.dumps(strcuture)
        ligand_to_insert = {
            "id": id,
            "Name": Name,
            "Solubility": Solubility,
            "LogP": LogP,
            "MolecularWeight": MolecularWeight,
            "IUPAC": IUPAC,
            "Strcuture": pickled_structure,
            "DrugScore": DrugScore,
            "DrugLike": DrugLike,
            "SmileFormat": SmileFormat,
            "MolecularFormula": MolecularFormula,
        }

        try:
            insert_res = self.Ligand_collection.insert_one(ligand_to_insert)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    # ======================================================================================================================= Protein
    def Protein_search(self, id, name):
        protein_to_find = {
            "id": id,
            "Name": name
        }
        search_res = self.Protein_collection.find_one(protein_to_find)
        if search_res:
            protein_id = search_res["id"]
            protein_name = search_res["Name"]
            pickled_structure = search_res["Structure"]
            fasta_format = search_res["FastaFormat"]

            structure = pickle.loads(pickled_structure)

            return protein_id, protein_name, structure, fasta_format
        else:
            return None

    def Protein_insert(self, id, Name, FastaFormat, PDB_id, Structure):
        pdb_parser = PDBParser()
        structure = pdb_parser.get_structure(id, Structure)
        pickled_structure = pickle.dumps(structure)
        protein_to_insert = {
            "id": id,
            "Name": Name,
            "Structure": pickled_structure,
            "FastaFormat": FastaFormat,
            "PDB_id": PDB_id,
        }
        try:
            insert_res = self.Protein_collection.insert_one(protein_to_insert)

            if insert_res:
                return "Added Successfully"
        except:
            return -1


# obj = crud()
# # # # # disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus = obj.Disease_search(602452, 'Colorectal cancer with chromosomal instability, somatic')
# # # # # print(disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus)
# # # res = obj.Protein_insert("2232", 'ddd', 'dsds', 'sds', "../PDB/static/upload/1zik.pdb")
# # res = obj.Ligand_insert("heba", "heba", None, -1.2, 507.4, None, "../PDB/static/upload/1zik.pdb", None, None,
# #                         "Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O", "C10H16N5O13P3")
# #
# protein_id, protein_name, structure, fasta_format = obj.Protein_search("1zik","gcn4-leucine zipper core mutant asn16lys in the dimeric state")
# print(protein_id, protein_name, structure, fasta_format)


from pymongo import MongoClient
import pickle
import nglview as nv

def Protein_search(Id, name):
    MONGODB_URL = "mongodb+srv://Al-Hassan:Bigdata1128@bigdataproject.nhz6c7e.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(MONGODB_URL)
    db = client.Diseasome

    Protein_collection = db.Protein

    protein_to_find = {
        "id": Id,
        "Name": name
    }
    search_res = Protein_collection.find_one(protein_to_find)
    if search_res:
        protein_id = search_res["id"]
        protein_name = search_res["Name"]
        pickled_structure = search_res["Structure"]
        fasta_format = search_res["FastaFormat"]

        return protein_id, protein_name, pickled_structure, fasta_format
    else:
        return None

protein_id, protein_name, pickled_structure, fasta_format = Protein_search("1zik", "gcn4-leucine zipper core mutant asn16lys in the dimeric state")
if protein_id:
    struc = pickle.loads(pickled_structure)
    view = nv.show_biopython(struc)
    view._remote_call('setSize', target='Widget', args=['600px', '400px'])  # Set the size of the viewer
    print(view)  # Display the viewer
else:
    print("Protein not found in the database.")
