from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('phoneNumber')
            raw_pass = form.cleaned_data.get('password')
            return redirect('product:home')
    else:
        form = UserRegisterForm()    
    return render(request, 'register.html', {'form':form})
