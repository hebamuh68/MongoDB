class Ligand(object):
    def __init__(self, ligand_collection):
        self.ligand = ligand_collection
        self.id = 0
        self.name = ""
        self.solubility = ""
        self.logp = 0.0
        self.molecular_weight = 0.0
        self.iupac = ""
        self.structure = None
        self.drug_score = 0.0
        self.drug_like = None
        self.mutagenecity = None
        self.tumorogenecity = None
        self.rep_effect = None
        self.smile_format = None
        self.molecular_formula = ""
        self.properties = ["id", "name", "solubility", "logp", "molecular weight",
                           "iupac", "structure", "drug score", "drug like", "mutagenecity",
                           "tumorogenecity", "rep effect", "smile format", "molecular formula"]

    def Insert_Ligand(self):
        ligand_document = {
            "id": self.id,
            "Name": self.name,
            "Solubility": self.solubility,
            "LogP": self.logp,
            "MolecularWeight": self.molecular_weight,
            "IUPAC": self.iupac,
            "Structure": self.structure,
            "DrugScore": self.drug_score,
            "DrugLike": self.drug_like,
            "Mutagenecity": self.mutagenecity,
            "Tumorogenecity": self.tumorogenecity,
            "RepEffect": self.rep_effect,
            "SmileFormat": self.smile_format,
            "MolecularFormula": self.molecular_formula
        }

        inserted_id = self.ligand.insert_one(ligand_document).inserted_id

        if inserted_id:
            return 1

    def Get_Ligand(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.ligand.find({filt: value}).sort("id")
            return results

        except:
            print("You entered a not existed property...")
            return -1

    def Update_Ligand(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.ligand.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.ligand.update_one({"id": id}, update_stmt)


class Protein(object):
    def __init__(self, protein_collection):
        self.protein = protein_collection
        self.pdb_id = 0
        self.id = 0
        self.name = ""
        self.structure = ""
        self.fasta = ""
        self.properties = ["pdb_id", "id", "name", "structure", "fasta"]

    def Insert_Protein(self):
        protein_document = {
            "PDB_id": self.pdb_id,
            "id": self.id,
            "Name": self.name,
            "Structure": self.structure,
            "FastaFormat": self.fasta,
        }

        inserted_id = self.protein.insert_one(protein_document).inserted_id

        if inserted_id:
            return 1

    def Get_Protein(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.protein.find({filt: value}).sort("id")
            return results

        except:
            print("You entered a not existed property...")
            return -1

    def Update_Protein(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.protein.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.protein.update_one({"id": id}, update_stmt)


class Disease(object):
    def __init__(self, disease_collection):
        self.disease = disease_collection
        self.id = 0
        self.name = ""
        self.pdb_fk = 0
        self.protein_seq = ""
        self.type = ""
        self.gene_seq = ""
        self.properties = ["id", "name", "pdb_fk", "protein_seq", "type", "gene_seq"]

    def Insert_Disease(self):
        disease_document = {
            "id": self.id,
            "Name": self.name,
            "PDB_fk": self.pdb_fk,
            "ProteinSeq": self.protein_seq,
            "Type": self.type,
            "GeneSeq": self.gene_seq,
        }

        inserted_id = self.disease.insert_one(disease_document).inserted_id

        if inserted_id:
            return 1

    def Get_Disease(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.disease.find({filt: value}).sort("id")
            return results

        except:
            print("You entered a not existed property...")
            return -1

    def Update_Disease(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.disease.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.disease.update_one({"id": id}, update_stmt)


class BioActivity(object):
    def __init__(self, bioActivity_collection):
        self.bio_activity = bioActivity_collection
        self.id = 0
        self.npl = ""
        self.kinase_inhibitor = ""
        self.icm = 0
        self.gpcr = ""
        self.ligand_fk = 0
        self.properties = ["id", "npl", "kinase_inhibitor", "icm", "gpcr", "ligand_fk"]

    def Insert_BioActivity(self):
        bioActivity_document = {
            "id": self.id,
            "NPL": self.npl,
            "KinaseInhibitor": self.kinase_inhibitor,
            "ICM": self.icm,
            "GPCR": self.gpcr,
            "Ligand_fk": self.ligand_fk,
        }

        inserted_id = self.bio_activity.insert_one(bioActivity_document).inserted_id

        if inserted_id:
            return 1

    def Get_BioActivity(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.bio_activity.find({filt: value}).sort("id")
            return results

        except:
            print("You entered a not existed property...")
            return -1

    def Update_BioActivity(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.bio_activity.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.bio_activity.update_one({"id": id}, update_stmt)



class Dock(object):
    def __init__(self, dock_collection):
        self.dock = dock_collection
        self.id = 0
        self.rmsd = 0
        self.binding_affinity = 0
        self.binding_free_energy = 0
        self.ligand_id = 0
        self.pdb_id = 0
        self.properties = ["id", "rmsd", "binding_affinity", "binding_free_energy", "ligand_id", "pdb_id"]

    def Insert_Dock(self):
        bioActivity_document = {
            "id": self.id,
            "RMSD": self.rmsd,
            "BindingAffinity": self.binding_affinity,
            "BindingFreeEnergy": self.binding_free_energy,
            "Ligand_id": self.ligand_id,
            "PDB_id": self.pdb_id,
        }

        inserted_id = self.dock.insert_one(bioActivity_document).inserted_id

        if inserted_id:
            return 1

    def Get_Dock(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.dock.find({filt: value}).sort("id")
            return results

        except:
            print("You entered a not existed property...")
            return -1

    def Update_Dock(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.dock.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.dock.update_one({"id": id}, update_stmt)
