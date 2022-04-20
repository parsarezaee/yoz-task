from django.http import HttpResponse
from django.shortcuts import redirect, render
from account.models import UserRegisterModel
from django.contrib import messages
from account.forms import UserProfileForm
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')


@login_required(login_url='product:home')
def checkout(request):
    return render(request, 'checkout.html')