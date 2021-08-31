from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import AppUser, Task_Category, Task
from .forms import RegistrationForm, RegistrationChangeForm

class AppUserAdmin(UserAdmin):
    add_form = RegistrationForm
    form = RegistrationChangeForm
    model = AppUser
    list_display = ['username', 'first_name','last_name','password1','password2','email','birth_date','profile_pic']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('email','birth_date','profile_pic')}),
    ) #this will allow to change these fields in admin module

# Register your models here.
admin.site.register(AppUser,AppUserAdmin)
admin.site.register(Task_Category)
admin.site.register(Task)