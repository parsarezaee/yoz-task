from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView



class SignUpView(CreateView):
    template_name = 'account/register.html'
    success_url = reverse_lazy('')
