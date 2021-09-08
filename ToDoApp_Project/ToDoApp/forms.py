from django import forms
from .models import AppUser,Task,Task_Category
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.http import HttpResponse

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
        #Task_CategoryForm.fields["category"].queryset = Task_Category.objects.filter(user = request.user)
        exclude = ['user'] #Excluded the user field and saved the current logged in user by creating an object instance[using form.save(commit = False)] in the view and overwriting the user with requet.user.
"""
If you don't exclude the user field from the form as done above, then you have to use this commented code to only give the option of choosing the current logged in user.
    def __init__(self, request, *args, **kwargs):
        super(Task_CategoryForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = AppUser.objects.filter(username=request.user)"""


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']
        #TaskForm.category.queryset = category.objects.filter()

    def __init__(self, AppUser, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Task_Category.objects.filter(user=AppUser)
        #self.fields['user'].queryset = AppUser.objects.filter(username=request.user)"""