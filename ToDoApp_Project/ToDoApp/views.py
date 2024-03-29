from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import RegistrationForm,RegistrationChangeForm,TaskForm,Task_CategoryForm
from .models import AppUser,Task,Task_Category
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('ToDoApp:categoryindex')
    template_name = 'signup.html'

"""class CategoryOwner(CreateView):
    model = Task_Category
    exclude = ['user']

    def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CategoryOwner(CreateView):
    
    def form_valid(self, form):
        Task_Category = form.save(commit=False)
        Task_Category.user = ToDoApp.objects.get(user=self.request.user)  # use your own profile here
        Task_Category.save()
        return HttpResponseRedirect(self.get_success_url())"""


@login_required(login_url = 'home')
def categoryindex(request):
    #task_category_list = Task_Category.objects.all()
    task_category_list = Task_Category.objects.filter(user = request.user)
    return render(request, 'ToDoApp/task_category_list.html', {'task_category_list': task_category_list})

@login_required(login_url = 'home')
def taskindex(request):
    #task_list = Task.objects.all()
    task_list = Task.objects.filter(user = request.user)
    return render(request, 'ToDoApp/task_list.html', {'task_list': task_list})
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['tasks'] = context['tasks'].filter(user=self.request.user)
        #context['count'] = context['tasks'].filter(complete=False).count()
        #return context

@login_required(login_url = 'home')
def create_category(request):
    upload = Task_CategoryForm()
    if request.method == 'POST':
        upload = Task_CategoryForm(request.POST, request.FILES)
        if upload.is_valid():
           obj = upload.save(commit=False) # Return an object without saving to the DB
           obj.user = request.user # Add an author field which will contain current user's id
           obj.save() # Save the final "real form" to the DB
           return redirect('ToDoApp:categoryindex')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/ToDoApp/categoryindex'}}">reload</a>""") #Have to check whether this works or not.
    else:
        return render(request, 'ToDoApp/category_upload_form.html', {'category_upload_form':upload})

@login_required(login_url = 'home')
def create_task(request):
    #upload = TaskForm()
    if request.method == 'POST':
        upload = TaskForm(request.user, request.POST or None)
        if upload.is_valid():
            obj = upload.save(commit=False) # Return an object without saving to the DB
            obj.user = request.user # The user field of the form will now contain current user's id. Could have also done: obj.user_id = request.user.id
            obj.save() # Save the final "real form" to the DB
            return redirect('ToDoApp:taskindex')
        else:
            return HttpResponse("<a href='/ToDoApp/task'>Your form is wrong, click to reload.</a>")
    else:
        upload = TaskForm(request.user)
        return render(request, 'ToDoApp/upload_form.html', {'upload_form':upload})

@login_required(login_url = 'home')
def update_category(request, task_category_id):
    task_category_id = int(task_category_id)
    try:
        task_sel = Task_Category.objects.get(id = task_category_id)
    except Task_Category.DoesNotExist:
        return redirect('ToDoApp: categoryindex')
    task_category_form = Task_CategoryForm(request.POST or None, instance = task_sel)
    if task_category_form.is_valid():
       obj = task_category_form.save(commit=False) # Return an object without saving to the DB
       obj.user = request.user # Add an author field which will contain current user's id
       obj.save() # Save the final "real form" to the DB
       return redirect('ToDoApp:categoryindex')
    return render(request, 'ToDoApp/category_upload_form.html', {'category_upload_form':task_category_form})

@login_required(login_url = 'home')
def update_task(request, task_id):
    task_id = int(task_id)
    try:
        task_sel = Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        return redirect('ToDoApp:taskindex')
    task_form = TaskForm(request.user, request.POST or None, instance = task_sel)
    if task_form.is_valid():
       obj = task_form.save(commit=False) # Return an object without saving to the DB
       obj.user = request.user # Add an author field which will contain current user's id
       obj.save() # Save the final "real form" to the DB
       return redirect('ToDoApp:taskindex')
    return render(request, 'ToDoApp/upload_form.html', {'upload_form':task_form})

@login_required(login_url = 'home')
def delete_category(request, task_category_id):
    task_category_id = int(task_category_id)
    try:
        task_sel = Task_Category.objects.get(id = task_category_id)
    except Task_Category.DoesNotExist:
        return redirect('ToDoApp:categoryindex')
    task_sel.delete()
    return redirect('ToDoApp:categoryindex')

@login_required(login_url = 'home')
def delete_task(request, task_id):
    task_id = int(task_id)
    try:
        task_sel = Task.objects.get(id = task_id)
    except Task.DoesNotExist:
        return redirect('ToDoApp:taskindex')
    task_sel.delete()
    return redirect('ToDoApp:taskindex')