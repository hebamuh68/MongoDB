from django.urls import path
from .views import Home_view, Protein_search_view, Disease_search_view, Protein_insert_view, Ligand_insert_view, Dock_insert_view, Disease_insert_view, BioActivity_insert_view


urlpatterns = [
    path('', Home_view, name='Home'),

    path('BioActivity_insert/', BioActivity_insert_view, name='BioActivity_insert'),

    path('Disease_search/', Disease_search_view, name='Disease_search'),
    path('Disease_insert/', Disease_insert_view, name='Disease_insert'),

    path('Dock_insert/', Dock_insert_view, name='Dock_insert'),

    path('Ligand_insert/', Ligand_insert_view, name='Ligand_insert'),

    path('Protein_search/', Protein_search_view, name='Protein_search'),
    path('Protein_insert/', Protein_insert_view, name='Protein_insert'),

]
