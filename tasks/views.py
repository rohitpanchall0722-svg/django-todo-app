from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
# Create your views here.

def home(request):
    tasks = Tasks.objects.all()
    return render(request, "tasks/home.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Tasks.objects.create(title=title, description="")

    return redirect("home")
def toggle_task(request,task_id):
    if request.method == "POST":
        task = get_object_or_404(Tasks, id=task_id)
        task.completed = not task.completed
        task.save() 
    return redirect("home")


def delete_task(request,task_id):
    if request.method == "POST":
        task = get_object_or_404(Tasks, id=task_id)
        task.delete()
    return redirect("home")
