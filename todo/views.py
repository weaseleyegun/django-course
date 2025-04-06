from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    #return HttpResponse("Todo List")
    todos = Todo.objects.all() #select * from Todo
    return render(request, "todo.html",{"todos": todos})

def todo_main(request):
    return HttpResponse("<h1>Todo Main Page</h1>")

def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return HttpResponse("없는 페이지 입니다.", status = 404)
    return render(request, "todo.html", {"todo":todo})

def todo_detail_name(request, name):
    todo = Todo.objects.filter(name__icontains=name)
    first = todo.first()
    last = todo.last()
    return render(request, "todo.html", {"todo":todo, "firist":first, "last": last})