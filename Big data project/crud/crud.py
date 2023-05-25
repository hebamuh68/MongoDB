from Bio.PDB import PDBIO
from pymongo import MongoClient
from Bio.PDB.PDBParser import PDBParser
import pickle
import json

from crud.Diseasome import Disease


# from Diseasome import Disease


class crud:

    def __init__(self):
        # Create connection
        ##MONGODB_URL = "mongodb+srv://name:password@bigdataproject.nhz6c7e.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient("localhost", 27017)
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

    def Disease_insert_many(self, file_path):
        try:
            with open(file_path) as f:
                data = json.load(f)

            insert_res = self.Disease_collection.insert_many(data)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    def Disease_search(self, id=None, name=None):

        if name == "":
            disease_to_find = {
                "id": id,
            }
        else:
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

    def Search_By_Disease_Name(self, disease_name=None):
        disease = Disease(self.Disease_collection)

        if disease_name:
            results = []
            all_documents = disease.Get_All(use_index=True)
            if all_documents != -1:
                for document in all_documents:
                    if disease_name.lower() in document["Name"].lower():
                        results.append(document)
                return results
            else:
                print("No data has been returned...")
                return -1

        else:
            return disease.Get_All(use_index=True)

    def Search_Disease_By_Name_And_Type(self, name, type):
        disease = Disease(self.Disease_collection)
        results = []
        all_documents = disease.Get_All(use_index=True)
        if all_documents != -1:
            for doc in all_documents:
                if name.lower() in doc["Name"].lower() and type.lower() in doc["Type"].lower():
                    results.append(doc)

            return results

        else:
            print("Something went wrong...")
            return -1

    def Aggregate_By_Disease_Name(self, type):
        pipeline = [
            {
                "$match": {"Type": "No Inheritance"}
            },
            {
                "$group": {"_id": "$Name"}
            }
        ]
        results = []
        for res in self.Disease_collection.aggregate(pipeline):
            results.append(res['_id'])

        return results

    def Disease_update_many(self, type, property, new_value):
        filter_criteria = {
            'Type': type
        }

        update_operation = {
            '$set': {
                property: new_value
            }
        }
        try:
            update_result = self.Disease_collection.update_many(filter_criteria, update_operation)

            if update_result:
                return "Updated Successfully"
        except:
            return -1

    # Dock =======================================================================================================================
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

    def Get_Property_Avg_By_Protein(self, protein_pdb_id, property_value="Binding Affinity"):
        pipeline = [
            {
                "$match": {"PDB_id": f"{protein_pdb_id}"}
            },
            {
                "$group": {
                    "_id": "$PDB_id",
                    "AVG": {"$avg": f"${property_value}"}
                }
            }
        ]

        results = []
        for res in self.Dock_collection.aggregate(pipeline):
            res['id'] = res.pop('_id')
            results.append(res)

        return results

    def Get_Property_Avg_By_Ligand(self, ligand_id, property_value="Binding Affinity"):
        pipeline = [
            {
                "$match": {"Ligand_id": ligand_id}
            },
            {
                "$group": {
                    "_id": "$Ligand_id",
                    "AVG": {"$avg": f"${property_value}"}
                }
            }
        ]

        results = []
        for res in self.Dock_collection.aggregate(pipeline):
            res['id'] = res.pop('_id')
            results.append(res)

        return results

    def Get_Docks_In_Property_Range(self, property_value="Intermolecular Contacts", value_range=[0, 5000]):
        results = []
        for res in self.Dock_collection.find(
                {f"{property_value}": {'$in': [x for x in range(value_range[0], value_range[1])]}}):
            results.append(res)

        return results

    # Ligand =======================================================================================================================
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

    def Ligand_insert_many(self, file_path):
        try:
            with open(file_path) as f:
                data = json.load(f)

            insert_res = self.Ligand_collection.insert_many(data)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    def Get_Ligand_Ids_By_BioActivity(self, type="IC50", value_range=[0, 10000]):
        results = []
        for res in self.BioActivity_collection.find(
                {"$and": [{f"{type}": {"$gt": value_range[0]}}, {f"{type}": {"$lt": value_range[1]}}]}):
            results.append(res["Ligand_fk"])

        return results

    # Protein =======================================================================================================================
    def Protein_search(self, id=None, name=None):
        if id == None:
            protein_to_find = {
                "Name": name
            }
        elif name == None:
            protein_to_find = {
                "id": id,
            }
        else:
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

            # Define the filename for the output text file
            output_name = f"PDB/static/upload/{protein_id}.pdb"
            structure_name = f"{protein_id}.pdb"

            # Save the structure as a PDB file
            pdb_io = PDBIO()
            pdb_io.set_structure(structure)
            pdb_io.save(output_name)

            return protein_id, protein_name, structure_name, fasta_format
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

    def Protein_insert_many(self, file_path):
        try:
            with open(file_path) as f:
                data = json.load(f)

            insert_res = self.Protein_collection.insert_many(data)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    def Protein_delete(self, id=None, Name=None):
        if id == None:
            protein_to_delete = {
                "Name": Name,
            }
        elif Name == None:
            protein_to_delete = {
                "id": id,
            }
        else:
            protein_to_delete = {
                "id": id,
                "Name": Name,
            }
        try:
            delete_res = self.Protein_collection.delete_one(protein_to_delete)
            if delete_res:
                return "Deleted Successfully"
        except:
            return -1
#
# obj = crud()
# protein_id, protein_name, structure_name, fasta_format = obj.Protein_search(name="gcn4-leucine zipper core mutant asn16lys in the dimeric state")
# print(protein_id, protein_name, structure_name, fasta_format)
# # #
# # # #protein_id, protein_name, structure_name, fasta_format = obj.Protein_search("1zik")
# # # protein_id, protein_name, structure_name, fasta_format = obj.Protein_search(name="gcn4-leucine zipper core mutant asn16lys in the dimeric state")
# # # print(protein_id, protein_name, structure_name, fasta_format)
