from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username':forms.TextInput(attrs = {'class':'form-control'}),
            'password1':forms.TextInput(attrs = {'class':'form-control'}),
            'password2':forms.TextInput(attrs = {'class':'form-control'}),
            'first_name':forms.TextInput(attrs = {'class':'form-control'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control'}),
            'email':forms.EmailInput(attrs = {'class':'form-control','placeholder':'ایمیل خود را وارد کنید' }),
            
        }

