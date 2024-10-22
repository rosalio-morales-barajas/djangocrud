from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TasksForm
from .models import Tasks
#import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'mensaje': 'El usuario ya existe...verifique!!!'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                "mensaje": 'Los passwords no coinciden...verifique!!!'
            })

@login_required
def tasks(request):
    tasks = Tasks.objects.filter(user=request.user, dateCompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
    
@login_required
def tasks_completed(request):
    tasks = Tasks.objects.filter(user=request.user, dateCompleted__isnull=False).order_by('-dateCompleted')
    return render(request, 'tasks.html', {
        'tasks': tasks
    })    

@login_required
def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'create_tasks.html', {
            'form': TasksForm
        })
    else:
        try:
            form = TasksForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_tasks.html', {
                'form': TasksForm,
                'mensaje': 'Error en los datos ingresados...verifique!!!'
            })
                       
@login_required          
def task_details(request):
    tasks = get_object_or_404(Tasks)
    return render(request, 'task_details.html', {
        'tasks': tasks
    })
    
@login_required               
def task_details(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Tasks, id=id, user=request.user)
        form = TasksForm(instance=task)
        return render(request, 'task_details.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Tasks, id=id, user=request.user)
            form = TasksForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            task = get_object_or_404(Tasks, id=id, user=request.user)
            form = TasksForm(instance=task)
            return render(request, 'task_details.html', {
                'task': task,
                'form': form,
                'error': 'There was occurred an error...verify it...'
            })
   
@login_required            
def complete_task(request, id):
    task = get_object_or_404(Tasks, id=id, user=request.user)
    if request.method == 'POST':
        task.dateCompleted = timezone.now()
        task.save()           
        return redirect('tasks')
  
@login_required   
def delete_task(request, id):
    task = get_object_or_404(Tasks, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()           
        return redirect('tasks')    
   
@login_required    
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'mensaje': 'El usuario o el password son incorrectos...verifique!!!...'
            })
        else:
            login(request, user)
            return redirect('tasks')
