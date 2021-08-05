from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, UserManager
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
class NewUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, blank=True, default='user')
    email =  models.EmailField(max_length=254, null=False, blank=False, unique=True)
    username = models.CharField(max_length=100, null=True, blank=False, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=False, default='1234')
    phone_number = models.CharField(max_length=10,unique=True, blank=False)
    address = models.CharField(max_length=100, blank=False)
    # USERNAME_FIELD = None
    def save(self,*args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
        super(NewUser, self).save(*args, **kwargs)
    
# class TaskUser(models.Model):
#     task = models.CharField(max_length=100, blank=True, default='')
#     description = models.TextField()
    
