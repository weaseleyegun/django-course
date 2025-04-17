from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views import View


def todo_list(request):
    #return HttpResponse("Todo List")
    todos = Todo.objects.all() #select * from Todo
    search = request.GET.get("search")
    if search:
        todos = todos.filter(name__icontains=search)
    print("Rendering todo/list")

    return render(request, "todo/todo.html",{"todos": todos})

def todo_main(request):
    print("Rendering todo/main")

    return HttpResponse("<h1>Todo Main Page</h1>")

def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return HttpResponse("없는 페이지 입니다.", status = 404)
    print("Rendering todo/detail")
    
    return render(request, "todo/todo.html", {"todo":todo})

def todo_detail_name(request, name):
    todos = Todo.objects.filter(name__icontains=name)
    first = todos.first()
    last = todos.last()
    print("Rendering todo/detail_name")
    return render(request, "todo/todo.html", {"todos":todos, "first":first, "last": last})


class TodoCreateView(View):

    def get(self, request):
        print("Rendering todo/create.html")
        return render(request, "todo/create.html")