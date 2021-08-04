from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    
class TaskUser(models.Model):
    task = models.CharField(max_length=100, blank=True, default='')
    email =  models.EmailField(max_length=254, null=False, blank=False, default='')
    description = models.TextField()
    
