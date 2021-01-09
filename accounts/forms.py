from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='اختیاری.',widget=TextInput(attrs={'class': 'form-control mt-2 d-block','placeholder': 'نام'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='اختیاری.',widget=TextInput(attrs={'class': 'form-control mt-2 d-block','placeholder': 'نام خانوادگی'}))
    email = forms.EmailField(max_length=254, required=True, help_text='اجباری',widget=EmailInput(attrs = {'class':'form-control mt-2 d-block','placeholder':'ایمیل' }))
    username = forms.TextInput()
    password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control mt-2 d-block','placeholder':'رمزعبور'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control mt-2 d-block','placeholder':'تایید رمز عبور'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username','password1', 'password2', )
        widgets = {
            'username':TextInput(attrs={'class':'form-control mt-2 d-block','placeholder':'نام کاربری'}),
        }


        
class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control mt-3','placeholder': 'نام کاربری'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control mt-3','placeholder':'رمز عبور'}))


