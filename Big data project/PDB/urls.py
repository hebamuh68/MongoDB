from django.urls import path

from .views import Home_view, Protein_search_view, Disease_search_view, Protein_insert_view, Ligand_insert_view, \
    Dock_insert_view, Disease_insert_view, BioActivity_insert_view, Avg_By_Protein_view, Avg_By_Ligand_view, \
    Docks_In_Property_Range_view, Ligand_In_Property_Range_view, Protein_insert_many_view, Ligand_insert_many_view, \
    Disease_insert_many_view, Protein_delete_view, Disease_update_many_view

urlpatterns = [
    path('', Home_view, name='Home'),

    path('BioActivity_insert/', BioActivity_insert_view, name='BioActivity_insert'),

    path('Disease_search/', Disease_search_view, name='Disease_search'),
    path('Disease_insert/', Disease_insert_view, name='Disease_insert'),
    path('Disease_insert_many/', Disease_insert_many_view, name='Disease_insert_many'),
    path('Disease_update_many/', Disease_update_many_view, name='Disease_update_many'),

    path('Dock_insert/', Dock_insert_view, name='Dock_insert'),
    path('Dock_property/', Docks_In_Property_Range_view, name='Dock_property'),


    path('Protein_search/', Protein_search_view, name='Protein_search'),
    path('Protein_insert/', Protein_insert_view, name='Protein_insert'),
    path('Protein_insert_many/', Protein_insert_many_view, name='Protein_insert_many'),
    path('Protein_delete/', Protein_delete_view, name='Protein_delete'),

    path('Avg_By_Protein/', Avg_By_Protein_view, name='Avg_By_Protein'),
    path('Avg_By_Ligand/', Avg_By_Ligand_view, name='Avg_By_Ligand'),

    path('Ligand_insert/', Ligand_insert_view, name='Ligand_insert'),
    path('Ligand_insert_many/', Ligand_insert_many_view, name='Ligand_insert_many'),
    path('Ligand_property/', Ligand_In_Property_Range_view, name='Ligand_property'),

]
