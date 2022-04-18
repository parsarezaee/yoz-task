from django import forms
from .models import UserRegisterModel
from django.forms import ModelForm


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = UserRegisterModel
        fields = '__all__'