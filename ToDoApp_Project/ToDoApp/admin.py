from django.contrib import admin
from .models import Task_Category, Task
from .models import Task
# Register your models here.
admin.site.register(Task_Category)
admin.site.register(Task)