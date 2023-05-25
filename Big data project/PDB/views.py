import os
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from PDB.forms import Protein_search_form, Protein_insert_form, Disease_search_form, Disease_insert_form, \
    Dock_insert_form, Ligand_insert_form, \
    BioActivity_insert_form, Avg_By_Protein_form, Avg_By_Ligand_form, Docks_In_Property_Range_form, \
    Ligand_In_Property_Range_form, Protein_insert_many_form, Ligand_insert_many_form, Disease_insert_many_form, \
    Protein_delete_form, Disease_update_many_form
from PDB.functions import handle_uploaded_file
from crud import crud
from crud.Diseasome import Disease

# initiate crud class
obj = crud.crud()


# Create your views here.
def Home_view(request):
    return render(request, 'Home.html')


# Bio Activity =======================================================================================================================
def BioActivity_insert_view(request):
    if request.method == 'POST':
        form = BioActivity_insert_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data['Id']
            IC50 = form.cleaned_data['IC50']
            Ki = form.cleaned_data['Ki']
            GI50 = form.cleaned_data['GI50']
            EC50 = form.cleaned_data['EC50']
            Kd = form.cleaned_data['Kd']
            Ligand_fk = form.cleaned_data['Ligand_fk']

            insert_res = obj.BioActivity_insert(Id, IC50, Ki, GI50, EC50, Kd, Ligand_fk)
            return render(request, 'BioActivity_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = form.errors
            return render(request, 'BioActivity_insert.html', {'form': form, "insert_res": insert_res})
    else:
        form = BioActivity_insert_form()
    return render(request, 'BioActivity_insert.html', {'form': form})


# Disease =======================================================================================================================
def Disease_search_view(request):
    if request.method == 'POST':
        form = Disease_search_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data['Id']
            Name = form.cleaned_data['Name']
            Type = form.cleaned_data['Type']

            # ===Search_Disease_By_Name_And_Type
            if (Type != "") and (Name != ""):
                type_docs = obj.Search_Disease_By_Name_And_Type(Name, Type)
                return render(request, 'Disease_search.html',
                              {'form': form, 'type_docs': type_docs})

            # ===Aggregate_By_Disease_Name
            elif (Type != "") and (Name == ""):
                Aggregate_docs = obj.Aggregate_By_Disease_Name(Type)
                return render(request, 'Disease_search.html',
                              {'form': form, 'Aggregate_docs': Aggregate_docs})

            # ===Search_By_Disease_Name
            elif Id == None:
                docs = obj.Search_By_Disease_Name(Name)
                return render(request, 'Disease_search.html',
                              {'form': form, 'docs': docs})

            # ===Search_By_Disease_Id
            elif Name == "":
                disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus = obj.Disease_search(
                    Id, Name)
                return render(request, 'Disease_search.html',
                              {'form': form, 'disease_id': disease_id, 'disease_name': disease_name, 'PDB_fk': PDB_fk,
                               'protein_seq': protein_seq, 'disease_type': disease_type, 'geneSeq': geneSeq,
                               'gene_locus': gene_locus})

            # ===Disease_search
            else:
                disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus = obj.Disease_search(
                    Id, Name)
                return render(request, 'Disease_search.html',
                              {'form': form, 'disease_id': disease_id, 'disease_name': disease_name, 'PDB_fk': PDB_fk,
                               'protein_seq': protein_seq, 'disease_type': disease_type, 'geneSeq': geneSeq,
                               'gene_locus': gene_locus})

        else:
            Search_result = form.errors
            return render(request, 'Disease_search.html', {'form': form, 'Search_result': Search_result})
    else:
        form = Disease_search_form()
    return render(request, 'Disease_search.html', {'form': form})


def Disease_insert_view(request):
    if request.method == 'POST':
        form = Disease_insert_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data["Id"]
            name = form.cleaned_data["Name"]
            pdb_fk = form.cleaned_data["PDB_fk"]
            protein_seq = form.cleaned_data["Protein_seq"]
            d_type = form.cleaned_data["disease_type"]
            gene_seq = form.cleaned_data["geneSeq"]
            gene_locus = form.cleaned_data["gene_locus"]

            insert_res = obj.Disease_insert(Id, name, pdb_fk, protein_seq, d_type, gene_seq, gene_locus)
            return render(request, 'Disease_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = form.errors
            return render(request, 'Disease_insert.html', {'form': form, "insert_res": insert_res})
    else:
        form = Disease_insert_form()
    return render(request, 'Disease_insert.html', {'form': form})


def Disease_insert_many_view(request):
    if request.method == 'POST':
        form = Disease_insert_many_form(request.POST, request.FILES)

        if form.is_valid():

            File_path = handle_uploaded_file(request.FILES['data_file'])
            insert_res = obj.Disease_insert_many(File_path)
            return render(request, 'Disease_insert_many.html', {'form': form, "insert_res": insert_res})
        else:
            insert_res = form.errors
            return render(request, 'Disease_insert_many.html', {'form': form, 'insert_res': insert_res})
    else:
        form = Disease_insert_many_form()
    return render(request, 'Disease_insert_many.html', {'form': form})


def Disease_update_many_view(request):
    if request.method == 'POST':
        form = Disease_update_many_form(request.POST)

        if form.is_valid():
            Type = form.cleaned_data["Type"]
            property = form.cleaned_data["property"]
            new_value = form.cleaned_data["new_value"]

            update_res = obj.Disease_update_many(Type, property, new_value)
            return render(request, 'Disease_update_many.html', {'form': form, "update_res": update_res})
        else:
            update_res = form.errors
            return render(request, 'Disease_update_many.html', {'form': form, 'update_res': update_res})
    else:
        form = Disease_update_many_form()
    return render(request, 'Disease_update_many.html', {'form': form})


# Dock =======================================================================================================================
def Dock_insert_view(request):
    if request.method == 'POST':
        form = Dock_insert_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data["Id"]
            Ligand_id = form.cleaned_data["Ligand_id"]
            PDB_id = form.cleaned_data["PDB_id"]
            intermolecular_contacts = form.cleaned_data["intermolecular_contacts"]
            charged_charged_contacts = form.cleaned_data["charged_charged_contacts"]
            charged_polar_contacts = form.cleaned_data["charged_polar_contacts"]
            charged_apolar_contacts = form.cleaned_data["charged_apolar_contacts"]
            polar_polar_contacts = form.cleaned_data["polar_polar_contacts"]
            aploar_polar_contacts = form.cleaned_data["aploar_polar_contacts"]
            apolar_apolar_contacts = form.cleaned_data["apolar_apolar_contacts"]
            dissociation_constant = form.cleaned_data["dissociation_constant"]
            binding_affinity = form.cleaned_data["binding_affinity"]
            charged_nis_residues_percentage = form.cleaned_data["charged_nis_residues_percentage"]
            aploar_nis_residues_percentage = form.cleaned_data["aploar_nis_residues_percentage"]

            insert_res = obj.Dock_insert(Id, intermolecular_contacts, charged_charged_contacts,
                                         charged_polar_contacts, charged_apolar_contacts, polar_polar_contacts,
                                         aploar_polar_contacts,
                                         apolar_apolar_contacts, binding_affinity, dissociation_constant,
                                         charged_nis_residues_percentage,
                                         aploar_nis_residues_percentage, Ligand_id, PDB_id)
            return render(request, 'Dock_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = form.errors
            return render(request, 'Dock_insert.html', {'form': form, "insert_res": insert_res})
    else:
        form = Dock_insert_form()
    return render(request, 'Dock_insert.html', {'form': form})


def Avg_By_Protein_view(request):
    if request.method == 'POST':
        form = Avg_By_Protein_form(request.POST)

        if form.is_valid():
            Protein_id = form.cleaned_data['protein_id']
            property = form.cleaned_data['my_choice']
            res = obj.Get_Property_Avg_By_Protein(Protein_id, property)
            return render(request, 'Avg_By_Protein.html', {'form': form, "res": res})
        else:
            res = form.errors
            return render(request, 'Avg_By_Protein.html', {'form': form, "res": res})
    else:
        form = Avg_By_Protein_form()
    return render(request, 'Avg_By_Protein.html', {'form': form})


def Avg_By_Ligand_view(request):
    if request.method == 'POST':
        form = Avg_By_Ligand_form(request.POST)

        if form.is_valid():
            Ligand_id = form.cleaned_data['Ligand_id']
            property = form.cleaned_data['my_choice']
            res = obj.Get_Property_Avg_By_Ligand(Ligand_id, property)
            return render(request, 'Avg_By_Ligand.html', {'form': form, "res": res})
        else:
            res = form.errors
            return render(request, 'Avg_By_Ligand.html', {'form': form, "res": res})
    else:
        form = Avg_By_Ligand_form()
    return render(request, 'Avg_By_Ligand.html', {'form': form})


def Docks_In_Property_Range_view(request):
    if request.method == 'POST':
        form = Docks_In_Property_Range_form(request.POST)

        if form.is_valid():
            my_choice = form.cleaned_data['my_choice']
            res = obj.Get_Docks_In_Property_Range(my_choice)
            return render(request, 'Dock_property.html', {'form': form, "res": res})
        else:
            res = form.errors
            return render(request, 'Dock_property.html', {'form': form, "res": res})
    else:
        form = Docks_In_Property_Range_form()
    return render(request, 'Dock_property.html', {'form': form})


# ======================================================================================================================= Ligand
def Ligand_insert_view(request):
    if request.method == 'POST':
        form = Ligand_insert_form(request.POST, request.FILES)

        if form.is_valid():
            Id = form.cleaned_data["Id"]
            Name = form.cleaned_data["Name"]
            Solubility = form.cleaned_data["Solubility"]
            LogP = form.cleaned_data["LogP"]
            MolecularWeight = form.cleaned_data["MolecularWeight"]
            IUPAC = form.cleaned_data["IUPAC"]
            Structure = handle_uploaded_file(request.FILES['structure'])
            DrugScore = form.cleaned_data["DrugScore"]
            DrugLike = form.cleaned_data["DrugLike"]
            SmileFormat = form.cleaned_data["SmileFormat"]
            MolecularFormula = form.cleaned_data["MolecularFormula"]

            insert_res = obj.Ligand_insert(Id, Name, Solubility, LogP, MolecularWeight, IUPAC, Structure, DrugScore,
                                           DrugLike,
                                           SmileFormat, MolecularFormula)
            return render(request, 'Ligand_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = form.errors
            return render(request, 'Ligand_insert.html', {'form': form, "insert_res": insert_res})
    else:
        form = Ligand_insert_form()
    return render(request, 'Ligand_insert.html', {'form': form})


def Ligand_insert_many_view(request):
    if request.method == 'POST':
        form = Ligand_insert_many_form(request.POST, request.FILES)

        if form.is_valid():

            File_path = handle_uploaded_file(request.FILES['data_file'])
            insert_res = obj.Ligand_insert_many(File_path)
            return render(request, 'Ligand_insert_many.html', {'form': form, "insert_res": insert_res})
        else:
            insert_res = form.errors
            return render(request, 'Ligand_insert_many.html', {'form': form, 'insert_res': insert_res})
    else:
        form = Ligand_insert_many_form()
    return render(request, 'Ligand_insert_many.html', {'form': form})


def Ligand_In_Property_Range_view(request):
    if request.method == 'POST':
        form = Ligand_In_Property_Range_form(request.POST)

        if form.is_valid():
            my_choice = form.cleaned_data['my_choice']
            res = obj.Get_Ligand_Ids_By_BioActivity(my_choice)
            return render(request, 'Ligand_property.html', {'form': form, "res": res})
        else:
            res = form.errors
            return render(request, 'Ligand_property.html', {'form': form, "res": res})
    else:
        form = Ligand_In_Property_Range_form()
    return render(request, 'Ligand_property.html', {'form': form})


# ======================================================================================================================= Protein
def Protein_search_view(request):
    if request.method == 'POST':
        form = Protein_search_form(request.POST)
        if form.is_valid():
            Id = form.cleaned_data['Id']
            Name = form.cleaned_data['Name']

            if Id == "" and Name == "":
                no_result = "Make sure ou entered valid data"
                return render(request, 'Protein_search.html', {'form': form, 'no_result': no_result})
            elif Id == "":
                protein_id, protein_name, structure_name, fasta_format = obj.Protein_search(name=Name)
            elif Name == "":
                protein_id, protein_name, structure_name, fasta_format = obj.Protein_search(id=Id)
            else:
                protein_id, protein_name, structure_name, fasta_format = obj.Protein_search(Id, Name)

            return render(request, 'Protein_search.html', {
                'form': form,
                'protein_id': protein_id,
                'protein_name': protein_name,
                'structure_name': structure_name,
                'fasta_format': fasta_format,
            })

        else:
            Search_result = form.errors
            return render(request, 'Protein_search.html', {'form': form, 'Search_result': Search_result})
    else:
        form = Protein_search_form()
    return render(request, 'Protein_search.html', {'form': form})


def Protein_insert_view(request):
    if request.method == 'POST':
        form = Protein_insert_form(request.POST, request.FILES)

        if form.is_valid():
            Id = form.cleaned_data['Id']
            Name = form.cleaned_data['Name']
            Structure = handle_uploaded_file(request.FILES['structure'])
            fasta_format = form.cleaned_data['fasta_format']
            PDB_id = form.cleaned_data['PDB_id']

            insert_res = obj.Protein_insert(Id, Name, fasta_format, PDB_id, Structure)
            return render(request, 'Protein_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = form.errors
            return render(request, 'Protein_insert.html', {'form': form, 'insert_res': insert_res})
    else:
        form = Protein_insert_form()
    return render(request, 'Protein_insert.html', {'form': form})


def Protein_insert_many_view(request):
    if request.method == 'POST':
        form = Protein_insert_many_form(request.POST, request.FILES)

        if form.is_valid():
            File_path = handle_uploaded_file(request.FILES['data_file'])
            insert_res = obj.Protein_insert_many(File_path)
            return render(request, 'Protein_insert_many.html', {'form': form, "insert_res": insert_res})
        else:
            insert_res = form.errors
            return render(request, 'Protein_insert_many.html', {'form': form, 'insert_res': insert_res})
    else:
        form = Protein_insert_many_form()
    return render(request, 'Protein_insert_many.html', {'form': form})


def Protein_delete_view(request):
    if request.method == 'POST':
        form = Protein_delete_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data['Id']
            Name = form.cleaned_data['Name']

            if Id == "" and Name == "":
                no_result = "Make sure ou entered valid data"
                return render(request, 'Protein_delete.html', {'form': form, 'no_result': no_result})
            elif Name == "":
                delete_res = obj.Protein_delete(id=Id)
            elif Id == "":
                delete_res = obj.Protein_delete(Name=Name)
            else:
                delete_res = obj.Protein_delete(Id, Name)
            return render(request, 'Protein_delete.html', {'form': form, "delete_res": delete_res})
        else:
            delete_res = form.errors
            return render(request, 'Protein_delete.html', {'form': form, 'delete_res': delete_res})
    else:
        form = Protein_delete_form()
    return render(request, 'Protein_delete.html', {'form': form})
