from django import forms
from .models import Task,Task_Category

class Task_CategoryForm(forms.ModelForm):

    class Meta:
        model = Task_Category
        fields = '__all__'

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        #exclude = ['duedate']