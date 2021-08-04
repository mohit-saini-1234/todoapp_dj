from django.contrib import admin

# Register your models here.
from todo_task.models import Task , TaskUser

admin.site.register(Task)
admin.site.register(TaskUser)
