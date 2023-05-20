import pickle

from pymongo import MongoClient
from django.shortcuts import render
from PDB.forms import Protein_search_form, Protein_insert_form, Disease_search_form, Disease_insert_form, \
    Dock_insert_form, Ligand_insert_form, \
    BioActivity_insert_form
from crud import crud

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
            insert_res = "Please make sure you entered valid data!"
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
            disease_id, disease_name, PDB_fk, protein_seq, disease_type, geneSeq, gene_locus = obj.Disease_search(Id,
                                                                                                                  Name)
            return render(request, 'Disease_search.html',
                          {'form': form, 'disease_id': disease_id, 'disease_name': disease_name, 'PDB_fk': PDB_fk,
                           'protein_seq': protein_seq, 'disease_type': disease_type, 'geneSeq': geneSeq,
                           'gene_locus': gene_locus})
        else:
            Search_result = "Please make sure you entered valid data!"
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
            insert_res = "Please make sure you entered valid data!"
            return render(request, 'Disease_insert.html', {'form': form, "insert_res": insert_res})
    else:
        form = Disease_insert_form()
    return render(request, 'Disease_insert.html', {'form': form})


# Dock =======================================================================================================================
def Dock_insert_view(request):
    if request.method == 'POST':
        form = Dock_insert_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data["Id"]
            RMSD = form.cleaned_data["RMSD"]
            BindingAffinity = form.cleaned_data["BindingAffinity"]
            BindingFreeEnergy = form.cleaned_data["BindingFreeEnergy"]
            Ligand_id = form.cleaned_data["Ligand_id"]
            PDB_id = form.cleaned_data["PDB_id"]

            insert_res = obj.Dock_insert(Id, RMSD, BindingAffinity, BindingFreeEnergy, Ligand_id, PDB_id)
            return render(request, 'Dock_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = "Please make sure you entered valid data!"
            return render(request, 'Dock_insert.html', {'form': form, "insert_res": insert_res})
    else:
        form = Dock_insert_form()
    return render(request, 'Dock_insert.html', {'form': form})


# ======================================================================================================================= Ligand
def Ligand_insert_view(request):
    if request.method == 'POST':
        form = Ligand_insert_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data["Id"]
            Name = form.cleaned_data["Name"]
            Solubility = form.cleaned_data["Solubility"]
            LogP = form.cleaned_data["LogP"]
            MolecularWeight = form.cleaned_data["MolecularWeight"]
            IUPAC = form.cleaned_data["IUPAC"]
            Strcuture = form.cleaned_data["Strcuture"]
            DrugScore = form.cleaned_data["DrugScore"]
            DrugLike = form.cleaned_data["DrugLike"]
            Mutagenecity = form.cleaned_data["Mutagenecity"]
            Tumorogenecity = form.cleaned_data["Tumorogenecity"]
            RepEffect = form.cleaned_data["RepEffect"]
            SmileFormat = form.cleaned_data["SmileFormat"]
            MolecularFormula = form.cleaned_data["MolecularFormula"]

            insert_res = obj.Ligand_insert(Id, Name, Solubility, LogP, MolecularWeight, IUPAC, Strcuture, DrugScore,
                                           DrugLike, Mutagenecity, Tumorogenecity, RepEffect, SmileFormat,
                                           MolecularFormula)
            return render(request, 'Ligand_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = "Please make sure you entered valid data!"
            return render(request, 'Ligand_insert.html', {'form': form, "insert_res": insert_res})
    else:
        form = Ligand_insert_form()
    return render(request, 'Ligand_insert.html', {'form': form})


# ======================================================================================================================= Protein
def Protein_search_view(request):
    if request.method == 'POST':
        form = Protein_search_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data['Id']
            Name = form.cleaned_data['Name']
            protein_id, protein_name, structure, fasta_format = obj.Protein_search(Id, Name)
            return render(request, 'Protein_search.html',
                          {'form': form, 'protein_id': protein_id, "protein_name": protein_name,
                           'fasta_format': fasta_format, 'structure': structure})
        else:
            Search_result = "Please make sure you entered valid data!"
            return render(request, 'Protein_search.html', {'form': form})
    else:
        form = Protein_search_form()
    return render(request, 'Protein_search.html', {'form': form})


def Protein_insert_view(request):
    if request.method == 'POST':
        form = Protein_insert_form(request.POST)

        if form.is_valid():
            Id = form.cleaned_data['Id']
            Name = form.cleaned_data['Name']
            structure = form.cleaned_data['structure']
            fasta_format = form.cleaned_data['fasta_format']
            PDB_id = form.cleaned_data['PDB_id']

            insert_res = obj.Ligand_insert(Id, Name, structure, fasta_format, PDB_id)
            return render(request, 'Protein_insert.html', {'form': form, "insert_res": insert_res})

        else:
            insert_res = "Please make sure you entered valid data!"
            return render(request, 'Protein_insert.html', {'form': form})
    else:
        form = Protein_insert_form()
    return render(request, 'Protein_insert.html', {'form': form})