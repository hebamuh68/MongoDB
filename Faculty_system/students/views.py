from django.shortcuts import render
from students.forms import search_form, insert_form
from Crud import Crud

# Create your views here.

def search_views(request):
    if request.method == 'POST':
        form = search_form(request.POST)

        if form.is_valid():
            Name = form.cleaned_data['Name']
            Grade = form.cleaned_data['Grade']

            crud = Crud.Crud()
            search_result = crud.Search_student(Name, Grade)
            return render(request, 'Search.html', {'form': form, 'search_result': search_result})
    else:
        form = search_form()

    return render(request, 'Search.html', {'form': form})


def insert_views(request):
    if request.method == 'POST':
        form = insert_form(request.POST)

        if form.is_valid():
            Name = form.cleaned_data['Name']
            Grade = form.cleaned_data['Grade']
            GPA = form.cleaned_data['GPA']

            crud = Crud.Crud()
            insert_result = crud.Insert_student(Name, Grade, GPA)
            return render(request, 'Insert.html', {'form': form, 'insert_result': "Added successful"})
    else:
        form = insert_form()

    return render(request, 'Insert.html', {'form': form})
