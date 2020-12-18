from django.forms import ModelForm, Textarea
from django import forms
from .models import PlanetData

#create the form class.

class Planet_Form(ModelForm):
    class Meta:
        model = PlanetData
        exclude = ['User', 'Categories', 'created_at', 'updated_at']
        widgets = {
            'Category':forms.TextInput(attrs = {'class':'form-control'}),
            'Name':forms.TextInput(attrs = {'class':'form-control'}),
            'Age_Stirng':forms.TextInput(attrs = {'class':'form-control'}),
            'Age_Numberic':forms.TextInput(attrs = {'class':'form-control'}),
            'Weather':forms.TextInput(attrs = {'class':'form-control'}),
            'Water':forms.TextInput(attrs = {'class':'form-control','placeholder':"نوع آبیاری"}),
            'Area':forms.TextInput(attrs = {'class':'form-control','placeholder':"مساحت مذرعه را وارد کنید."}),
        }

          
