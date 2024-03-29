from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class SignUpForm(UserChangeForm):
    name=forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label='Email Adress', widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('name',  'email', 'username', 'password1', 'password2')