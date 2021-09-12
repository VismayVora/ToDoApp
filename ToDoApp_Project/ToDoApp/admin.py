from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import AppUser, Task_Category, Task
from .forms import RegistrationForm, RegistrationChangeForm, Task_CategoryForm

class AppUserAdmin(UserAdmin):
    add_form = RegistrationForm
    form = RegistrationChangeForm
    model = AppUser
    list_display = ['username', 'first_name','last_name','email','birth_date','profile_pic']
    search_fields = ['username', 'first_name','last_name','email']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('birth_date','profile_pic')}),
    ) #this will allow to change these fields in admin module

class Task_CategoryAdmin(admin.ModelAdmin):
    #add_form = Task_CategoryForm
    #form = Task_CategoryForm
    model = Task
    list_display = ('user','title','description')
    #fieldsets = (
    #        (None, {'fields': ('user','title','description')}),
    #)
    search_fields = ['title','description']

    """def save_model(self, request, obj, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.user:
            instance.created_by = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance"""

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('user','category','title','description','priority_no','status','duedate')
    fieldsets = (
            (None, {'fields': ('user','category','title','description','priority_no','status','duedate')}),
    )
    search_fields = ['title','description']
    """def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)"""
    """def save_model(self, request, obj, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.user:
            instance.user = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance"""


# Register your models here.
admin.site.register(AppUser,AppUserAdmin)
admin.site.register(Task_Category,Task_CategoryAdmin)
admin.site.register(Task,TaskAdmin)

