from django.forms import ModelForm
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class search_form(forms.Form):
    Name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Student Name',
                                                         'style': 'width: 400px; border-top-left-radius: 25px; '
                                                                  'border-bottom-left-radius: 25px; '
                                                                  'padding: 10px;'}))
    Grade = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)],
                               widget=forms.TextInput(attrs={'placeholder': 'Student Grade',
                                                             'style': 'width: 200px;''padding: 10px;'}))


class insert_form(forms.Form):
    Name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Student Name',
                         'style': 'width: 400px; ''border-radius: 15px; ''padding: 10px; margin:10px'}))

    Grade = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)],
                               widget=forms.TextInput(attrs={'placeholder': 'Student Grade',
                                'style': 'width: 400px; ''border-radius: 15px; ''padding: 10px; margin:10px'}))

    GPA = forms.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(4.0)],
                           widget=forms.TextInput(attrs={'placeholder': 'Student GPA',
                         'style': 'width: 400px; ''border-radius: 15px; ''padding: 10px; margin:10px'}))
