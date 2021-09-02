from django.urls import path
from . import views
from .views import SignUpView
from ToDoApp_Project.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', views.categoryindex, name = 'categoryindex'),
    path('task/', views.taskindex, name = 'taskindex'),
    path('upload/', views.create_category, name = 'create-category'),
    path('task/upload/', views.create_task, name = 'create-task'),
    path('update/<int:task_category_id>', views.update_category),
    path('task/update/<int:task_id>', views.update_task),
    path('delete/<int:task_category_id>', views.delete_category),
    path('task/delete/<int:task_id>', views.delete_task)
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
