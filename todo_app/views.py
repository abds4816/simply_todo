from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .models import Task

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

@require_http_methods(['POST'])
def add_task(request):
    title = request.POST['title']
    if title:
        Task.objects.create(title=title)
    return redirect('/')

def complete_task(request, id):
    Task.objects.filter(id=id).update(is_done=True)
    return redirect('/')

def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('/')