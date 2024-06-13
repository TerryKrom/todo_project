from django.shortcuts import render, redirect, get_object_or_404
from tasks.model.models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')


def remove_tag(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    print(task)
    task.delete()
    return redirect('task_list')

