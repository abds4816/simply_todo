from asyncio import tasks
from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)