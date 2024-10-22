
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('task_details/', views.task_details, name='task_details'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('task_details/<int:id>/', views.task_details, name='task_details'),
    path('task_details/<int:id>/complete', views.complete_task, name='complete_task'),
    path('task_details/<int:id>/delete', views.delete_task, name='delete_task'),
]
