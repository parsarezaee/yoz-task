from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register', views.signup, name='register'),
    path('login', views.UserLoginView.as_view(), name='login')
]
