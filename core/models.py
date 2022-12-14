from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class user(AbstractBaseUser):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    is_ambassador=models.BooleanField(default=True)
    username= None

    USERNAME_FIELD='email'
    REQUIRED_FIELD=[]
