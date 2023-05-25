from crud import crud
import pymongo
from Diseasome import *

diseasome = crud()

def Create_Index_On_Protein(user_property):
    protein = Protein(diseasome.Protein_collection)
    for prop in protein.properties:
        if user_property.lower() == prop.lower() or user_property.lower() in prop.lower():
            property_index = prop
            break
    try:
        diseasome.Protein_collection.create_index([(f"{property_index}", pymongo.ASCENDING)])
        print("Index added successfully...")
    except:
        return -1

def Create_Index_On_Disease(user_property):
    disease = Disease(diseasome.Disease_collection)
    for prop in disease.properties:
        if user_property.lower() == prop.lower() or user_property.lower() in prop.lower():
            property_index = prop
            break
    try:
        diseasome.Disease_collection.create_index([(f"{property_index}", pymongo.ASCENDING)])
        print("Index added successfully...")
    except:
        return -1

def Create_Index_On_Dock(user_property):
    dock = Dock(diseasome.Dock_collection)
    for prop in dock.properties:
        if user_property.lower() == prop.lower() or user_property.lower() in prop.lower():
            property_index = prop
            break
    try:
        diseasome.Dock_collection.create_index([(f"{property_index}", pymongo.ASCENDING)])
        print("Index added successfully...")
    except:
        return -1

def Create_Index_On_Ligand(user_property):
    ligand = Ligand(diseasome.Ligand_collection)
    for prop in ligand.properties:
        if user_property.lower() == prop.lower() or user_property.lower() in prop.lower():
            property_index = prop
            break
    try:
        diseasome.Ligand_collection.create_index([(f"{property_index}", pymongo.ASCENDING)])
        print("Index added successfully...")
    except:
        return -1

def Create_Index_On_BioActivity(user_property):
    bioactivity = BioActivity(diseasome.BioActivity_collection)
    for prop in bioactivity.properties:
        if user_property.lower() == prop.lower() or user_property.lower() in prop.lower():
            property_index = prop
            break
    try:
        diseasome.BioActivity_collection.create_index([(f"{property_index}", pymongo.ASCENDING)])
        print("Index added successfully...")
    except:
        return -1
    
Create_Index_On_Protein(user_property="Name")
Create_Index_On_Disease(user_property="Name")