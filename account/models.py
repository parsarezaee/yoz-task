from django.db import models
from django.core.validators import RegexValidator


class UserRegisterModel(models.Model):
    #register user with phone number
    phoneNumberRegex = RegexValidator(regex= r"09[0-3][0-9]-?[0-9]{3}-?[0-9]{4}")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    password = models.CharField(max_length=100)