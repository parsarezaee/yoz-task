from django import forms
from .models import UserRegisterModel
from django.forms import ModelForm


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', 
    widget= forms.PasswordInput)
    class Meta:
        model = UserRegisterModel
        fields = ['phoneNumber', 'password']