from django.contrib import admin

# Register your models here.
from user.models import NewUser

admin.site.register(NewUser)