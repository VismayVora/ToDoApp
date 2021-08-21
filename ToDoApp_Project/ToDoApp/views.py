from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.http import HttpResponse
# Create your views here.

def index(request):
    task_list = Task.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

def create_task(request):
    upload = TaskForm()
    if request.method == 'POST':
        upload = TaskForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
else:
        return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_task(request, task_id):
    task_id = int(task_id)
    try:
        task_sel = Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        return redirect('index')
    task_form = TaskForm(request.POST or None, instance = task_sel)
    if task_form.is_valid():
       task_form.save()
       return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form':task_form})

def delete_task(request, task_id):
    task_id = int(task_id)
    try:
        task_sel = Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        return redirect('index')
    task_sel.delete()
    return redirect('index')