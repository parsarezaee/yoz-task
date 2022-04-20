from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('checkout', views.checkout, name='checkout')
]
