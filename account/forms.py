from django import forms
from .models import UserRegisterModel, UserProfileModel
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = UserRegisterModel
        fields = ('phone',)

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    phone = forms.RegexField(regex= r"^09\d{2}\s*?\d{3}\s*?\d{4}$")
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)


    class Meta:
        model = UserProfileModel
        fields = ('first_name', 'last_name', 'email')
