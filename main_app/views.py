from django.shortcuts import render, HttpResponseRedirect
from .models import Ambition, Todo


# Create your views here.
def index(request):
    return render(request, 'indexMain.html')


def add_ambition(request):
    return render(request, 'addAmbition.html')


def submitted_ambition(request):
    ambition = Ambition(name=request.GET.get("Name"), description=request.GET.get("desc"),
                        dueDate=request.GET.get("date"))
    ambition.save()
    return HttpResponseRedirect("/")


def add_todo(request, name):
    todo = Todo(name=name)
    todo.save()
    return HttpResponseRedirect("/")


def remove_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")
