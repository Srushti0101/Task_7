from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import RegisterForm, TaskForm
from .models import Task


def home(request):
    return redirect('dashboard' if request.user.is_authenticated else 'login')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Account created! Please log in.")
        return redirect('login')
    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)      # only MY tasks
    total = tasks.count()
    done = tasks.filter(done=True).count()
    return render(request, 'dashboard.html', {
        'tasks': tasks, 'total': total, 'done': done,
        'pending': total - done, 'form': TaskForm(),
    })


@login_required
@require_POST
def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user                         # associate with user
        task.save()
    return redirect('dashboard')


@login_required
@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)   # 404 if not owner
    task.done = not task.done
    task.save()
    return redirect('dashboard')


@login_required
@require_POST
def delete_task(request, pk):
    get_object_or_404(Task, pk=pk, user=request.user).delete()
    return redirect('dashboard')