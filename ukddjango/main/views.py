from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'To do Today', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Error'

    form = TaskForm()
    contex = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', contex)
