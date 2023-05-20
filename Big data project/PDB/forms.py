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
    RMSD = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'RMSD',
                                                            'style': 'width: 400px;''padding: 10px;'}))
    BindingAffinity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Binding Affinity',
                                                                       'style': 'width: 400px;''padding: 10px;'}))
    BindingFreeEnergy = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Binding Free Energy',
                                                                         'style': 'width: 400px;''padding: 10px;'}))
    Ligand_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Ligand Id',
                                                                 'style': 'width: 400px;''padding: 10px;'}))
    PDB_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'PDB id',
                                                              'style': 'width: 400px;''padding: 10px;'}))


# ======================================================================================================================= Ligand
class Ligand_insert_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ligand Name',
                                                         'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                  'border-bottom-left-radius: 25px; '
                                                                  'padding: 10px;'}))
    Id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Ligand Id',
                                                          'style': 'width: 200px;''padding: 10px;'}))
    Solubility = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Solubility',
                                                               'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                        'border-bottom-left-radius: 25px; '
                                                                        'padding: 10px;'}))
    LogP = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'LogP',
                                                            'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                     'border-bottom-left-radius: 25px; '
                                                                     'padding: 10px;'}))
    MolecularWeight = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Molecular Weight',
                                                                       'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                                'border-bottom-left-radius: 25px; '
                                                                                'padding: 10px;'}))
    IUPAC = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'IUPAC',
                                                          'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                   'border-bottom-left-radius: 25px; '
                                                                   'padding: 10px;'}))
    Strcuture = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Struture',
                                                             'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                      'border-bottom-left-radius: 25px; '
                                                                      'padding: 10px;'}))
    DrugScore = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Drug Score',
                                                                 'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                          'border-bottom-left-radius: 25px; '
                                                                          'padding: 10px;'}))
    DrugLike = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Drug Like',
                                                             'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                      'border-bottom-left-radius: 25px; '
                                                                      'padding: 10px;'}))
    Mutagenecity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mutagenecity',
                                                                 'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                          'border-bottom-left-radius: 25px; '
                                                                          'padding: 10px;'}))
    Tumorogenecity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tumorogenecity',
                                                                   'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                            'border-bottom-left-radius: 25px; '
                                                                            'padding: 10px;'}))
    RepEffect = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Rep Effect',
                                                              'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                       'border-bottom-left-radius: 25px; '
                                                                       'padding: 10px;'}))
    SmileFormat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Smile Format',
                                                                'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                         'border-bottom-left-radius: 25px; '
                                                                         'padding: 10px;'}))
    MolecularFormula = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Molecular Formula',
                                                                     'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                              'border-bottom-left-radius: 25px; '
                                                                              'padding: 10px;'}))


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
                                                         'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                  'border-bottom-left-radius: 25px; '
                                                                  'padding: 10px;'}))
    Id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Id',
                                                       'style': 'width: 200px;''padding: 10px;'}))
    structure = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'structure',
                                                              'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                       'border-bottom-left-radius: 25px; '
                                                                       'padding: 10px;'}))
    fasta_format = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Fasta format',
                                                                 'style': 'width: 200px;''padding: 10px;'}))
    PDB_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'PDB_id',
                                                           'style': 'width: 200px;''padding: 10px;'}))
