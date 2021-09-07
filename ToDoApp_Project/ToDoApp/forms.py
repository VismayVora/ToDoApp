from django import forms
from .models import AppUser,Task,Task_Category
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class RegistrationForm(UserCreationForm):
   
    class Meta(UserCreationForm):
        model = AppUser
        #fields = ('username','first_name','last_name','password1','password2','email','birth_date','profile_pic')
        fields = ['username','first_name','last_name','email','birth_date','profile_pic']
        #fields = ('username','first_name','last_name','email')
        #fields = UserCreationForm.Meta.fields + ('birth_date','profile_pic')

class RegistrationChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = AppUser
        #fields = ('username','first_name','last_name','password1','password2','email','birth_date','profile_pic')
        fields = ('username','first_name','last_name','email','birth_date','profile_pic')
        #fields = ('username','first_name','last_name','email')
        #fields = UserCreationForm.Meta.fields + ('birth_date','profile_pic')

class Task_CategoryForm(forms.ModelForm):

    class Meta:
        model = Task_Category
        fields = '__all__'
        exclude = ['user']

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        #exclude = ['user']