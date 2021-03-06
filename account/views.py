from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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





class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'login.html'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username= cd['phone'], password= cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('product:home')
            messages.error(request, 'Phone number or password is wrong', 'warning')
        return render(request, self.template_name, {'form':form})



class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You logged out successfuly', 'success')
        return redirect('product:home')


@login_required(login_url='product:home')
def userprofile(request):
    #complete profile by user
    if request.method == 'POST':
        user_form = UserProfileForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile completed successfuly')
        else:
            messages.error(request, 'error completing your profile')
    else:
        user_form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'user_form':user_form})