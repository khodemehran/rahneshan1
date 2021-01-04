from django.forms import ModelForm, Textarea, EmailInput,TextInput
from django import forms
from .models import userinput


class userinput(ModelForm):
    
    name = forms.CharField(widget=TextInput(attrs={'class':'form-control mt-2 d-block','placeholder':'نام'}))
    Roshd_date = forms.EmailField(widget=EmailInput(attrs={'class':'form-control mt-2 d-block','placeholder':'ایمیل'}))

    class Meta:
        model = userinput
        fields = (
                  'name',
                  'Roshd_date',
                 )
