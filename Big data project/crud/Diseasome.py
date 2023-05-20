"""
    The Diseasome.py script contains each collection from the Diseasome mongo database as a class and they are:
        Disease, Protein, Dock, Ligand, BioActivity.
    Each class contains the CRUD operations for each collection to manipulate the data in the database.

"""
class Protein(object):
    """
        The Protein class is responsible for dealing with the CRUD operations for the Protein collection in the Diseasome database.
        Each object from this class contains the properties of the collection as object attributes which are:
            "id": the PDB id for that protein,
            "name": the protein name,
            "structure": the protein 3D structure,
            "fasta": the fasta format for the protein sequence.
            As well the object contains the attribute protein which is the mongo collection cursor to access the collection in the
            database and it must be passed in the object declaration,
            finally the attribute properties which holds the collection properties to help doing the CRUD without errors.
        Thus dealing with Protein collection requires you to declare an object of this class...     

    """
    def __init__(self, protein_collection):
        self.protein = protein_collection
        self.id = ""
        self.name = ""
        self.structure = None
        self.fasta = ""
        self.properties = ["id", "name", "structure", "fasta"]

    ##Pre-conditions: a declared object from the Protein class with mongo Protein collection passed in object declaration and 
    # object attributes are populated with data otherwise, the document will be filled with empty values...
    ##Post-conditions:  1 will be returned if values inserted correctly otherwise -1 will be returned...
    def Insert_Protein(self):
        protein_document = {
            "id": self.id,
            "Name": self.name,
            "Structure": self.structure,
            "FastaFormat": self.fasta,
        }

        try:
            inserted_id = self.protein.insert_one(protein_document).inserted_id
            if inserted_id:
                return 1
            
        except:
            return -1
    
    ##Pre-conditions: a declared object from the Protein class with mongo Protein collection passed in object declaration, a property
    # and its value must be passed to the Get function...
    ##Post-conditions: a list of the returned documents if the query values exist, otherwise -1 if not exist...
    def Get_Protein(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.protein.find({filt: value}).sort("id")
            returned_values = []
            for result in results:
                returned_values.append(result)
            return returned_values

        except:
            print("You entered a non existed property...")
            return -1
        
    ##Pre-conditions: a declared object from the Protein class with mongo Protein collection passed in object declaration, a property
    # and its value must be passed to the Update function but at first you have to pass the id of the wanted document...
    ##Post-conditions: a document will be updated according to the passed parameters...
    def Update_Protein(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.protein.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.protein.update_one({"id": id}, update_stmt)
    
    ##Pre-conditions: a declared object from the Protein class with mongo Protein collection passed in object declaration, the id
    # of the wanted document must be passed...
    ##Post-conditions: a document will be deleted according to the passed parameters, otherwise -1 will be returned...
    def Delete_Protein(self, id):
        try:
            self.protein.delete_one({"id":id})
        except:
            return -1

class BioActivity(object):
    """
        The BioActivity class is responsible for dealing with the CRUD operations for the BioActivity collection in the Diseasome database.
        Each object from this class contains the properties of the collection as object attributes which are:
            "id": we will use the uniport id to distinguish the documents,
            "ic50": it indicates how much drug is needed to inhibit a biological process by half, 
                    thus providing a measure of potency of an antagonist drug in pharmacological research
            "ki": is an indication of how potent an inhibitor is; it is the concentration required to produce half maximum inhibition,
            "gi50": represents the concentration of a drug that reduces total cell growth by 50%,
            "ec50":the concentration (or dose) effective in producing 50% of the maximal response,
                   and is a convenient way of comparing drug potencies
            "kd":the ratio of the antibody dissociation rate (koff), how quickly it dissociates from its antigen, to the antibody association 
                 rate (kon) of the antibody, how quickly it binds to its antigen
            "ligand_fk": the ligand id from the Ligand collection.
            As well the object contains the attribute bio_activity which is the mongo collection object to access the collection in the
            database and it must be passed in the object declaration,
            finally the attribute properties which holds the collection properties to help doing the CRUD without errors.
        Thus dealing with BioActivity collection requires you to declare an object of this class...

    """
    def __init__(self, bioActivity_collection):
        self.bio_activity = bioActivity_collection
        self.id = 0
        self.ic50 = 0.0
        self.ki = 0.0
        self.gi50 = 0
        self.ec50 = 0.0
        self.kd = 0.0
        self.ligand_fk = 0
        self.properties = ["id", "ic50", "ki", "gi50", "ec50", "kd", "ligand_fk"]

    ##Pre-conditions: a declared object from the BioActivity class with mongo BioActivity collection passed in object declaration and 
    # object attributes are populated with data otherwise, the document will be filled with empty values...
    ##Post-conditions:  1 will be returned if values inserted correctly otherwise -1 will be returned..
    def Insert_BioActivity(self):
        bioActivity_document = {
            "id": self.id,
            "IC50": self.ic50,
            "Ki": self.ki,
            "GI50": self.gi50,
            "EC50": self.ec50,
            "Kd": self.kd,
            "Ligand_fk": self.ligand_fk,
        }

        try:
            inserted_id = self.bio_activity.insert_one(bioActivity_document).inserted_id

            if inserted_id:
                return 1
            
        except:
            return -1

    ##Pre-conditions: a declared object from the BioActivity class with mongo BioActivity collection passed in object declaration,
    # a property and its value must be passed to the Get function...
    ##Post-conditions: a list of the returned documents if the query values exist, otherwise -1 if not exist...
    def Get_BioActivity(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.bio_activity.find({filt: value}).sort("id")
            returned_values = []
            for result in results:
                returned_values.append(result)

            return returned_values

        except:
            print("You entered a not existed property...")
            return -1

    ##Pre-conditions: a declared object from the BioActivity class with mongo BioActivity collection passed in object declaration, a property
    # and its value must be passed to the Update function but at first you have to pass the id of the wanted document...
    ##Post-conditions: a document will be updated according to the passed parameters...
    def Update_BioActivity(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.bio_activity.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.bio_activity.update_one({"id": id}, update_stmt)

    ##Pre-conditions: a declared object from the BioActivity class with mongo BioActivity collection passed in object declaration,
    # the id of the wanted document must be passed...
    ##Post-conditions: a document will be deleted according to the passed parameters, otherwise -1 will be returned...
    def Delete_BioActivity(self, id):
        try:
            self.bio_activity.delete_one({"id":id})
        except:
            return -1
        
class Disease(object):
    """
        The Disease class is responsible for dealing with the CRUD operations for the Disease collection in the Diseasome database.
        Each object from this class contains the properties of the collection as object attributes which are:
            "id": the omim number provided,
            "name": the disease name, 
            "pdb_fk": the PDB id of the protein associated with the disease,
            "protein_seq": the protein sequence,
            "type": the disease inheritance type or no inheritance,
            "gene_seq": the gene sequence, 
            As well the object contains the attribute disease which is the mongo collection object to access the collection in the
            database and it must be passed in the object declaration,
            finally the attribute properties which holds the collection properties to help doing the CRUD without errors.
        Thus dealing with Disease collection requires you to declare an object of this class...     

    """
    def __init__(self, disease_collection):
        self.disease = disease_collection
        self.id = 0
        self.name = ""
        self.pdb_fk = 0
        self.protein_seq = ""
        self.type = ""
        self.gene_seq = ""
        self.properties = ["id", "name", "pdb_fk", "protein_seq", "type", "gene_seq"]

    ##Pre-conditions: a declared object from the Disease class with mongo Disease collection passed in object declaration and 
    # object attributes are populated with data otherwise, the document will be filled with empty values...
    ##Post-conditions:  1 will be returned if values inserted correctly otherwise -1 will be returned..
    def Insert_Disease(self):
        disease_document = {
            "id": self.id,
            "Name": self.name,
            "PDB_fk": self.pdb_fk,
            "ProteinSeq": self.protein_seq,
            "Type": self.type,
            "GeneSeq": self.gene_seq,
        }
        
        try:
            inserted_id = self.disease.insert_one(disease_document).inserted_id

            if inserted_id:
                return 1
        except:
            return -1

    ##Pre-conditions: a declared object from the Disease class with mongo Disease collection passed in object declaration,
    # a property and its value must be passed to the Get function...
    ##Post-conditions: a list of the returned documents if the query values exist, otherwise -1 if not exist...
    def Get_Disease(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.disease.find({filt: value}).sort("id")
            returned_values = []
            for result in results:
                returned_values.append(result)

            return results

        except:
            print("You entered a not existed property...")
            return -1

    ##Pre-conditions: a declared object from the Disease class with mongo Disease collection passed in object declaration, 
    # a property and its value must be passed to the Update function but at first you have to pass the id of the wanted document...
    ##Post-conditions: a document will be updated according to the passed parameters...
    def Update_Disease(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.disease.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.disease.update_one({"id": id}, update_stmt)

    ##Pre-conditions: a declared object from the Disease class with mongo Disease collection passed in object declaration,
    # the id of the wanted document must be passed...
    ##Post-conditions: a document will be deleted according to the passed parameters, otherwise -1 will be returned...
    def Delete_Disease(self, id):
        try:
            self.disease.delete_one({"id":id})
        except:
            return -1


class Dock(object):
    """
        The Dock class is responsible for dealing with the CRUD operations for the Dock collection in the Diseasome database.
        Each object from this class contains the properties of the collection as object attributes which are:
            "id": self.id,
            "Intermolecular Contacts": number of intermolecular contacts,
            "Charged-Charged_Contacts": number of charged charged contacts,
            "Charged-Polar-Contacts": number of charged polar contacts,
            "Charged-Apolar-Contacts": number of charged apolar contacts,
            "Polar-Polar-Contacts": number of polar polar contacts,
            "Apolar-Polar-Contacts": number of apolar polar contacts,
            "Apolar-Apolar-Contacts": number of apolar apolar contacts,
            "Dissociation Constant": Dissociation constant,
            "Binding Affinity": Binding affinity,
            "Charged NIS Residues Percentage": Apolar NIS residues percentage,
            "Apolar NIS Residues Percentage": Charged NIS residues percentage,
            "Ligand_id": Ligand id from the ligand collection,
            "PDB_id": the PDB id from the Protein collection,
            As well the object contains the attribute dock which is the mongo collection object to access the collection in the
            database and it must be passed in the object declaration,
            finally the attribute properties which holds the collection properties to help doing the CRUD without errors.
        Thus dealing with Dock collection requires you to declare an object of this class...     
    """
    def __init__(self, dock_collection):
        self.dock = dock_collection
        self.id = 0
        self.num_of_itermolecular_contacts = 0
        self.binding_affinity = 0.0
        self.num_of_charged_charged_contacts = 0
        self.num_of_charged_polar_contacts = 0
        self.num_of_charged_apolar_contacts = 0
        self.num_of_polar_polar_contacts = 0
        self.num_of_apolar_polar_contacts = 0
        self.num_of_apolar_apolar_contacts = 0
        self.apolar_nis_residues_percentage = 0.0
        self.charged_nis_residues_percentage = 0.0
        self.dissociation_constant = 0.0
        self.ligand_id = 0
        self.pdb_id = 0
        self.properties = ["id", "rmsd", "binding_affinity", "binding_free_energy", "ligand_id", "pdb_id"]

    ##Pre-conditions: a declared object from the Dock class with mongo Dock collection passed in object declaration and 
    # object attributes are populated with data otherwise, the document will be filled with empty values...
    ##Post-conditions:  1 will be returned if values inserted correctly otherwise -1 will be returned..
    def Insert_Dock(self):
        bioActivity_document = {
            "id": self.id,
            "Intermolecular Contacts":self.num_of_itermolecular_contacts,
            "Charged-Charged_Contacts":self.num_of_charged_charged_contacts,
            "Charged-Polar-Contacts":self.num_of_charged_polar_contacts,
            "Charged-Apolar-Contacts":self.num_of_charged_apolar_contacts,
            "Polar-Polar-Contacts":self.num_of_polar_polar_contacts,
            "Apolar-Polar-Contacts":self.num_of_apolar_polar_contacts,
            "Apolar-Apolar-Contacts":self.num_of_apolar_polar_contacts,
            "Dissociation Constant":self.dissociation_constant,
            "Binding Affinity": self.binding_affinity,
            "Charged NIS Residues Percentage":self.charged_nis_residues_percentage,
            "Apolar NIS Residues Percentage":self.apolar_nis_residues_percentage,
            "Ligand_id": self.ligand_id,
            "PDB_id": self.pdb_id,
        }
        try:
            inserted_id = self.dock.insert_one(bioActivity_document).inserted_id

            if inserted_id:
                return 1
        except:
            return -1

    ##Pre-conditions: a declared object from the Dock class with mongo Dock collection passed in object declaration,
    # a property and its value must be passed to the Get function...
    ##Post-conditions: a list of the returned documents if the query values exist, otherwise -1 if not exist...
    def Get_Dock(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.dock.find({filt: value}).sort("id")
            returned_values = []
            for result in results:
                returned_values.append(result)
            
            return returned_values

        except:
            print("You entered a not existed property...")
            return -1
        
    ##Pre-conditions: a declared object from the Dock class with mongo Dock collection passed in object declaration, 
    # a property and its value must be passed to the Update function but at first you have to pass the id of the wanted document...
    ##Post-conditions: a document will be updated according to the passed parameters...
    def Update_Dock(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.dock.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.dock.update_one({"id": id}, update_stmt)
    
    ##Pre-conditions: a declared object from the Dock class with mongo Dock collection passed in object declaration,
    # the id of the wanted document must be passed...
    ##Post-conditions: a document will be deleted according to the passed parameters, otherwise -1 will be returned...
    def Delete_Dock(self, id):
        try:
            self.dock.delete_one({"id":id})
        except:
            return -1


class Ligand(object):
    """
        The Ligand class is responsible for dealing with the CRUD operations for the Ligand collection in the Diseasome database.
        Each object from this class contains the properties of the collection as object attributes which are:
            "id": the ligand id from chembl,
            "Name": the ligand name,
            "Solubility": property of a substance (solute) to dissolve in a given solvent,
            "LogP": determines how well a drug will be absorbed, transported, and distributed in the body 
                    but also dictates how a drug should be formulated and dosed,
            "MolecularWeight": the ligand molecular weight,
            "IUPAC": the iupac formula of the ligand,
            "Structure": the structure of the ligand,
            "DrugScore": determines the likeless of the ligand as a drug,
            "DrugLike": assesses qualitatively the chance for a molecule to become an oral drug with respect to bioavailability,
            "SmileFormat": the smile format of the ligand,
            "MolecularFormula": the ligand molecular formula.
            As well the object contains the attribute ligand which is the mongo collection object to access the collection in the
            database and it must be passed in the object declaration,
            finally the attribute properties which holds the collection properties to help doing the CRUD without errors.
        Thus dealing with Ligand collection requires you to declare an object of this class...     
    """
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
        self.smile_format = None
        self.molecular_formula = ""
        self.properties = ["id", "name", "solubility", "logp", "molecular weight",
                           "iupac", "structure", "drug score", "drug like", "mutagenecity",
                           "tumorogenecity", "rep effect", "smile format", "molecular formula"]

    ##Pre-conditions: a declared object from the Ligand class with mongo Ligand collection passed in object declaration and 
    # object attributes are populated with data otherwise, the document will be filled with empty values...
    ##Post-conditions:  1 will be returned if values inserted correctly otherwise -1 will be returned..
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
            "SmileFormat": self.smile_format,
            "MolecularFormula": self.molecular_formula
        }

        try:
            inserted_id = self.ligand.insert_one(ligand_document).inserted_id

            if inserted_id:
                return 1
        except:
            return -1

    ##Pre-conditions: a declared object from the Ligand class with mongo Ligand collection passed in object declaration,
    # a property and its value must be passed to the Get function...
    ##Post-conditions: a list of the returned documents if the query values exist, otherwise -1 if not exist...
    def Get_Ligand(self, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            results = self.ligand.find({filt: value}).sort("id")
            returned_values = []
            for result in results:
                returned_values.append[result]
            
            return returned_values

        except:
            print("You entered a not existed property...")
            return -1

    ##Pre-conditions: a declared object from the Ligand class with mongo Ligand collection passed in object declaration, 
    # a property and its value must be passed to the Update function but at first you have to pass the id of the wanted document...
    ##Post-conditions: a document will be updated according to the passed parameters...
    def Update_Ligand(self, id, property, value):
        try:
            filt_index = self.properties.index(property)

            filt = self.properties[filt_index]
            update_stmt = {"$set": {filt: value}}
            self.ligand.update_one({"id": id}, update_stmt)

        except:
            update_stmt = {"$set": {property: value}}
            self.ligand.update_one({"id": id}, update_stmt)

    ##Pre-conditions: a declared object from the Ligand class with mongo Ligand collection passed in object declaration,
    # the id of the wanted document must be passed...
    ##Post-conditions: a document will be deleted according to the passed parameters, otherwise -1 will be returned...
    def Delete_Ligand(self, id):
        try:
            self.ligand.delete_one({"id":id})
        except:
            return -1



