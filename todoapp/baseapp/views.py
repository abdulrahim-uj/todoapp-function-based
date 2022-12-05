from django.shortcuts import render, redirect
from . models import Task
from . forms import TodoTaskForm


def index(request):
    form = TodoTaskForm()
    data = Task.objects.all()
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baseapp:home')
        else:
            print("Something went wrong!")

        context = {
            'project': "ToDo App",
            'title': "Home",
            'tasks': data,
        }
        return render(request, "baseapp/index.html", context=context)
    else:
        context = {
            'project': "ToDo App",
            'title': "Home",
            'tasks': data,
            'form': form,
        }
        return render(request, "baseapp/index.html", context=context)


def delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        # SET is_deleted True; better than delete entire row from db
        # task.is_deleted = True
        # task.save()

        task.delete()
        return redirect('baseapp:home')
    else:
        context = {
            'project': "ToDo App",
            'title': "Delete",
        }
        return render(request, "baseapp/delete.html", context=context)


def changestatus(request, pk):
    # status set to 1 for completed task and save
    data = Task.objects.get(pk=pk)
    data.status = 1
    data.save()
    return redirect('baseapp:home')


def edittask(request, pk):
    instance = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoTaskForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('baseapp:home')
        else:
            print("Something went wrong")
    else:
        form = TodoTaskForm(request.POST or None, instance=instance)
        context = {
            'project': "ToDo App",
            'title': "Update Task",
            'form': form,
        }
        return render(request, "baseapp/edit_task_detail.html", context=context)
