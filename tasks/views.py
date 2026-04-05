from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from django.http import JsonResponse

def api_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)

def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)

    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"tasks": tasks})