from django.forms import ModelForm, Textarea, EmailInput,TextInput
from django import forms
from .models import PlanetData, Contact

#create the form class.

class Planet_Form(ModelForm):
    class Meta:
        model = PlanetData
        fields = ['Category','Name','Age_Stirng','Age_Numberic','Weather','Water','Area']
        widgets = {
            'Category':forms.Select(attrs = {'class':'form-control'}),
            'Name':forms.TextInput(attrs = {'class':'form-control'}),
            'Age_Stirng':forms.TextInput(attrs = {'class':'form-control'}),
            'Age_Numberic':forms.TextInput(attrs = {'class':'form-control'}),
            'Weather':forms.Select(attrs = {'class':'form-control'}),
            'Water':forms.Select(attrs = {'class':'form-control','placeholder':"نوع آبیاری"}),
            'Area':forms.TextInput(attrs = {'class':'form-control','placeholder':"مساحت مذرعه را وارد کنید."}),
        }

class ContactForm(ModelForm):
    
    content = forms.CharField(widget=Textarea(attrs={'class':'form-control mt-2 d-block','placeholder':'درخواست'}))
    name = forms.CharField(widget=TextInput(attrs={'class':'form-control mt-2 d-block','placeholder':'نام'}))
    Email_field = forms.EmailField(widget=EmailInput(attrs={'class':'form-control mt-2 d-block','placeholder':'ایمیل'}))

    class Meta:
        model = Contact
        fields = ('Email_field',
                  'name',
                  'content',
                 )

          
