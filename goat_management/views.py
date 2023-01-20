from django.shortcuts import HttpResponseRedirect, render

from goat_management.models import (Employee, FDead, Female, FSold, Male,
                                    Mating, MDead, MSold, Todo)

from .add_ons import Add_On_1
from .models import Acaricide, Dewormer, Drug, Employee, Feed, Others, Vaccine


# Create your views here.
def index(request, search=None):
    add_on = Add_On_1()
    male_num, female_num = Add_On_1.available(check_dead_or_sold)
    female = Female.objects.all()
    male = Male.objects.all()
    todo = Todo.objects.all()
    goats = concat(female, male)
    label, data = add_on.piechart()
    income, expenditure = add_on.totals()
    total = len(goats)
    emp = Employee.objects.all()
    context = {"female": female,
               "income": income,
               "expenditure": expenditure,
               "male": male,
               "preg": Add_On_1.is_pregnant,
               "male_num": male_num,
               "female_num": female_num,
               "todos": todo,
               "total": total,
               "employees": emp,
               "label": label,
               "data": data,
               "all": goats}

    if search == "bred":
        mates = Mating.objects.filter(male=request.GET.get("bred")) \
            if Mating.objects.filter(male=request.GET.get("bred")) \
            else Mating.objects.filter(female=request.GET.get("bred"))
        context = {"female": female,
                   "male": male,
                   "todos": todo,
                   "total": total,
                   "all": goats,
                   "employees": emp,
                   "mates": mates}

    if search == "goat":
        goats = search_for(request=request.GET.get(
            "attr"), query=request.GET.get("goat"))
        context = {"female": female,
                   "male": male,
                   "todos": todo,
                   "total": total,
                   "employees": emp,
                   "all": goats}

    return render(request, 'indexGoats.html', context)


def search_for(query, request):
    if request == "":
        request = "Id"
    if request == "Id":
        male = Male.objects.filter(id=query)
        female = Female.objects.filter(id=query)
        return concat(male, female)
    elif request == "Mother":
        male = Male.objects.filter(mother=query)
        female = Female.objects.filter(mother=query)
        return concat(male, female)
    elif request == "Father":
        male = Male.objects.filter(father=query)
        female = Female.objects.filter(father=query)
        return concat(male, female)
    elif request == "Category":
        male = Male.objects.filter(category=query)
        female = Female.objects.filter(category=query)
        return concat(male, female)
    elif request == "Estimated delivery date":
        male = None
        female = Female.objects.filter(estDob=query)
        return concat(male, female)
    elif request == "Date of birth":
        male = Male.objects.filter(dob=query)
        female = Female.objects.filter(dob=query)
        return concat(male, female)


def concat(obj1, obj2):
    l = []
    for i in obj1:
        if check_dead_or_sold(i.id):
            l.append(i)
    for i in obj2:
        if check_dead_or_sold(i.id):
            l.append(i)

    return l


def add_todo(request, name):
    todo = Todo(name=name)
    todo.save()
    return HttpResponseRedirect("/goats")


def remove_todo(request, name):
    todo = Todo.objects.get(name=name)
    todo.delete()
    return HttpResponseRedirect("/goats")


def check_dead_or_sold(id):
    if FDead.objects.filter(f_id=id) or MDead.objects.filter(m_id=id) or MSold.objects.filter(m_id=id) or FSold.objects \
            .filter(f_id=id):
        return False
    return True


def summary(request, target=None):
    expenditure = []
    all = [*Drug.objects.all(), *Employee.objects.all(), *Feed.objects.all(), *Vaccine.objects.all(),
           *Dewormer.objects.all(), *Acaricide.objects.all(), *Others.objects.all(),]
    context = {
        "model": Add_On_1.model_expenditure_choice(target),
        "models": Add_On_1.total_expenditure(),
        "add_on": Add_On_1(),
        "all": all,
        "total": Add_On_1.exp_totals(Add_On_1.total_expenditure()),
        "tables": ["None", "Drug", "Acaricide", "Dewormer", "Employee", "Vaccine", "Feeds", "Others"]
    }
    return render(request, 'summary.html', context)


def redirect_to_summary(request):
    return HttpResponseRedirect("/goats/summary")


def toggle_todo(request, name, checked):
    todo = Todo(name=name, complete=checked.capitalize())
    todo.save()
    return HttpResponseRedirect("/goats")
