from django.forms import ModelForm
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


# Bio Activity =======================================================================================================================

class BioActivity_insert_form(forms.Form):
    Id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'BioActivity Id',
                                                       'style': 'width: 400px;''padding: 10px;'}))
    IC50 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'IC50',
                                                            'style': 'width: 400px;''padding: 10px;'}))

    Ki = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Ki',
                                                          'style': 'width: 400px;''padding: 10px;'}))

    GI50 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'GI50',
                                                            'style': 'width: 400px;''padding: 10px;'}))

    EC50 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'EC50',
                                                            'style': 'width: 400px;''padding: 10px;'}))
    Kd = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Kd',
                                                          'style': 'width: 400px;''padding: 10px;'}))
    Ligand_fk = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ligand_fk',
                                                              'style': 'width: 800px;''padding: 10px;'}))


# Disease =======================================================================================================================

class Disease_search_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Disease Name',
                                                         'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                  'border-bottom-left-radius: 25px; '
                                                                  'padding: 10px;'}))
    Id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Disease Id',
                                                          'style': 'width: 200px;''padding: 10px;'}))


class Disease_insert_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                         'style': 'width: 400px;''padding: 10px;'}))
    Id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Id',
                                                          'style': 'width: 400px;''padding: 10px;'}))
    PDB_fk = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'PDB_fk',
                                                           'style': 'width: 400px;''padding: 10px;'}))
    Protein_seq = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Protein seq',
                                                                'style': 'width: 800px;''padding: 10px;'}))
    disease_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Disease type',
                                                                 'style': 'width: 400px;''padding: 10px;'}))
    geneSeq = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Gene seq',
                                                            'style': 'width: 800px;''padding: 10px;'}))
    gene_locus = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Gene locus',
                                                               'style': 'width: 800px;''padding: 10px;'}))


# Dock =======================================================================================================================
class Dock_insert_form(forms.Form):
    Id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Dock Id',
                                                          'style': 'width: 400px;''padding: 10px;'}))
    intermolecular_contacts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'intermolecular contacts',
                                                                               'style': 'width: 400px;''padding: 10px;'}))
    charged_charged_contacts = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'charged charged contacts',
                                      'style': 'width: 400px;''padding: 10px;'}))
    charged_polar_contacts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'charged polar contacts',
                                                                              'style': 'width: 400px;''padding: 10px;'}))
    charged_apolar_contacts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'charged apolar contacts',
                                                                               'style': 'width: 400px;''padding: 10px;'}))
    polar_polar_contacts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'polar polar contacts',
                                                                            'style': 'width: 400px;''padding: 10px;'}))
    aploar_polar_contacts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'aploar polar contacts',
                                                                             'style': 'width: 400px;''padding: 10px;'}))
    apolar_apolar_contacts = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'apolar apolar contacts',
                                                                              'style': 'width: 400px;''padding: 10px;'}))
    dissociation_constant = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'dissociation constant',
                                                                             'style': 'width: 400px;''padding: 10px;'}))
    binding_affinity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'binding affinity',
                                                                        'style': 'width: 400px;''padding: 10px;'}))
    charged_nis_residues_percentage = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'charged nis residues percentage',
                                      'style': 'width: 400px;''padding: 10px;'}))
    aploar_nis_residues_percentage = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'aploar nis residues percentage',
                                      'style': 'width: 400px;''padding: 10px;'}))
    Ligand_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Ligand Id',
                                                                 'style': 'width: 400px;''padding: 10px;'}))
    PDB_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'PDB id',
                                                              'style': 'width: 400px;''padding: 10px;'}))


# ======================================================================================================================= Ligand
class Ligand_insert_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ligand Name',
                                                         'style': 'width: 400px;''padding: 10px;'}))
    Id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ligand Id',
                                                          'style': 'width: 400px;''padding: 10px;'}))
    Solubility = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Solubility',
                                                               'style': 'width: 400px;''padding: 10px;'}), required=False)
    LogP = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'LogP',
                                                            'style': 'width: 400px;''padding: 10px;'}))
    MolecularWeight = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Molecular Weight',
                                                                       'style': 'width: 400px;''padding: 10px;'}))
    IUPAC = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'IUPAC',
                                                          'style': 'width: 400px;''padding: 10px;'}), required=False)
    DrugScore = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Drug Score',
                                                                 'style': 'width: 400px;''padding: 10px;'}), required=False)
    DrugLike = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Drug Like',
                                                             'style': 'width: 400px;''padding: 10px;'}), required=False)
    SmileFormat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Smile Format',
                                                                'style': 'width: 400px;''padding: 10px;'}))
    MolecularFormula = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Molecular Formula',
                                                                     'style': 'width: 400px;''padding: 10px;'}))
    structure = forms.FileField()


# ======================================================================================================================= Protein
class Protein_search_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Protein Name',
                                                         'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                  'border-bottom-left-radius: 25px; '
                                                                  'padding: 10px;'}))
    Id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Protein Id',
                                                       'style': 'width: 200px;''padding: 10px;'}))


class Protein_insert_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                         'style': 'width: 400px;''padding: 10px;'}))
    Id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Id',
                                                       'style': 'width: 400px;''padding: 10px;'}))
    fasta_format = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Fasta format',
                                                                 'style': 'width: 400px;''padding: 10px;'}))
    PDB_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'PDB_id',
                                                           'style': 'width: 400px;''padding: 10px;'}))
    structure = forms.FileField()
