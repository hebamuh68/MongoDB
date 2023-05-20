from pymongo import MongoClient


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
    def Dock_insert(self, id, RMSD, BindingAffinity, BindingFreeEnergy, Ligand_id, PDB_id):
        dock_to_insert = {
            "id": id,
            "RMSD": RMSD,
            "BindingAffinity": BindingAffinity,
            "BindingFreeEnergy": BindingFreeEnergy,
            "Ligand_id": Ligand_id,
            "PDB_id": PDB_id
        }
        try:
            insert_res = self.Dock_collection.insert_one(dock_to_insert)

            if insert_res:
                return "Added Successfully"
        except:
            return -1

    # ======================================================================================================================= Ligand
    def Ligand_insert(self, id, Name, Solubility, LogP, MolecularWeight, IUPAC, Strcuture, DrugScore, DrugLike,
                      Mutagenecity, Tumorogenecity, RepEffect, SmileFormat, MolecularFormula):
        ligand_to_insert = {
            "id": id,
            "Name": Name,
            "Solubility": Solubility,
            "LogP": LogP,
            "MolecularWeight": MolecularWeight,
            "IUPAC": IUPAC,
            "Strcuture": Strcuture,
            "DrugScore": DrugScore,
            "DrugLike": DrugLike,
            "Mutagenecity": Mutagenecity,
            "Tumorogenecity": Tumorogenecity,
            "RepEffect": RepEffect,
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
            structure = search_res["Structure"]
            fasta_format = search_res["FastaFormat"]

            return protein_id, protein_name, structure, fasta_format
        else:
            return None

    def Protein_insert(self, id, Name, Structure, FastaFormat, PDB_id):
        protein_to_insert = {
            "id": id,
            "Name": Name,
            "Structure": Structure,
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
# disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus = obj.Disease_search(602452, 'Colorectal cancer with chromosomal instability, somatic')
# print(disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus)
