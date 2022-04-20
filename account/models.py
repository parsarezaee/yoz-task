from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):
    """Define a model manager for user model with no username field"""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a user with the given phone numebr and password"""
        if not phone:
            raise ValueError('The given phone number must be set')
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self, phone, password=None, **extra_fields):
        """create and save a superuser with the diven phone number and password"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a superuser with the given phone number and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser=True!')
        
        return self._create_user(phone, password, **extra_fields)
    


class UserRegisterModel(AbstractUser):
    #register user with phone number
    username = None
    phone_number_Regex = RegexValidator(regex= r"^09\d{2}\s*?\d{3}\s*?\d{4}$")
    phone = models.CharField(validators = [phone_number_Regex], max_length = 11, unique = True, null=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.phone)


class UserProfileModel(models.Model):
    user = models.ForeignKey(UserRegisterModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_complete = models.BooleanField(default=False)
