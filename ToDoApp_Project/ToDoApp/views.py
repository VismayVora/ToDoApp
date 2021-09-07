from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import RegistrationForm,RegistrationChangeForm,TaskForm,Task_CategoryForm
from .models import AppUser,Task,Task_Category
from django.http import HttpResponse
# Create your views here.

class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('ToDoApp:categoryindex')
    template_name = 'signup.html'


def categoryindex(request):
    #task_category_list = Task_Category.objects.all()
    task_category_list = Task_Category.objects.filter(user = request.user)
    return render(request, 'ToDoApp/task_category_list.html', {'task_category_list': task_category_list})

def taskindex(request):
    task_list = Task.objects.filter()
    #task_list = Task.objects.filter(category = request.user.category)
    return render(request, 'ToDoApp/task_list.html', {'task_list': task_list})
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['tasks'] = context['tasks'].filter(user=self.request.user)
        #context['count'] = context['tasks'].filter(complete=False).count()
        #return context

def create_category(request):
    upload = Task_CategoryForm()
    if request.method == 'POST':
        upload = Task_CategoryForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('ToDoApp:categoryindex')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'categoryindex'}}">reload</a>""")
    else:
        return render(request, 'ToDoApp/category_upload_form.html', {'category_upload_form':upload})

def create_task(request):
    upload = TaskForm()
    if request.method == 'POST':
        upload = TaskForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('ToDoApp:taskindex')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'ToDoApp/upload_form.html', {'upload_form':upload})

def update_category(request, task_category_id):
    task_category_id = int(task_category_id)
    try:
        task_sel = Task_Category.objects.get(id = task_category_id)
    except Task_Category.DoesNotExist:
        return redirect('ToDOApp: categoryindex')
    task_category_form = Task_CategoryForm(request.POST or None, instance = task_sel)
    if task_category_form.is_valid():
       task_category_form.save()
       return redirect('ToDoApp:categoryindex')
    return render(request, 'ToDoApp/category_upload_form.html', {'category_upload_form':task_category_form})

def update_task(request, task_id):
    task_id = int(task_id)
    try:
        task_sel = Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        return redirect('ToDoApp:taskindex')
    task_form = TaskForm(request.POST or None, instance = task_sel)
    if task_form.is_valid():
       task_form.save()
       return redirect('ToDoApp:taskindex')
    return render(request, 'ToDoApp/upload_form.html', {'upload_form':task_form})

def delete_category(request, task_category_id):
    task_category_id = int(task_category_id)
    try:
        task_sel = Task_Category.objects.get(id = task_category_id)
    except Task_Category.DoesNotExist:
        return redirect('ToDoApp:categoryindex')
    task_sel.delete()
    return redirect('ToDoApp:categoryindex')

def delete_task(request, task_id):
    task_id = int(task_id)
    try:
        task_sel = Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        return redirect('ToDoApp:taskindex')
    task_sel.delete()
    return redirect('ToDoApp:taskindex')