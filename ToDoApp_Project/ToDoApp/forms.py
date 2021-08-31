from django import forms
from .models import AppUser,Task,Task_Category
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        #fields = ('username','first_name','last_name','password1','password2','email','birth_date','profile_pic')
        fields = UserCreationForm.Meta.fields + ('email','birth_date','profile_pic')

class RegistrationChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = AppUser
        #fields = ('username','first_name','last_name','password1','password2','email','birth_date','profile_pic')
        fields = UserCreationForm.Meta.fields + ('email','birth_date','profile_pic')

class Task_CategoryForm(forms.ModelForm):

    class Meta:
        model = Task_Category
        fields = '__all__'

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        #exclude = ['duedate']