from django.forms import ModelForm, Textarea, EmailInput,TextInput
from django import forms
from .models import userinput


class userinputform(ModelForm):
    
  # name = forms.CharField(widget=TextInput(attrs={'class':'form-control mt-2 d-block','placeholder':'نام گیاه'}))
   # Roshd_date = forms.EmailField(widget=EmailInput(attrs={'class':'form-control mt-2 d-block','placeholder':'مرحله رشد'}))

    class Meta:
        model = userinput
        fields = (
                  'name',
                  'Roshd_date',
                 )
        widgets = {
            'name':forms.Select(attrs = {'class':'form-control text-right','placeholder':"نام گیاه"}),
            'Roshd_date':forms.Select(attrs = {'class':'form-control text-right','placeholder':"مرحله رشد "}),
        }

                 
