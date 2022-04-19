from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from account.models import UserRegisterModel
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm





def signup(request):
    #signup user with phone number
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('product:home')
        messages.error(request, "Invalid registration")
    form = UserRegisterForm()    
    return render(request, 'registration/register.html', {'form':form})



# def login_user(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('phoneNumber')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             if user is None:
#                 login(request, user)
#                 messages.info(request, "You are now logged in")
#                 return redirect('product:home')
#             else:
#                 messages.error(request, "Invalid phone number or password")
#         else:
#             messages.error(request, "invalid phone number or password")
#     form = AuthenticationForm()
#     return render(request=request, template_name='login.html', context={'form':form})