from django.db import models
from django.core.validators import RegexValidator


class UserRegisterModel(models.Model):
    #register user with phone number
    phoneNumberRegex = RegexValidator(regex= r"^09\d{2}\s*?\d{3}\s*?\d{4}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.phoneNumber