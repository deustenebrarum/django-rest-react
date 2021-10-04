from django.shortcuts import render, redirect
from api.models import Employee
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")

def landing(request):
    return render(request, "landing.html")

def sert(request):
    return render(request, "sert.html")

def employees(request):
    if not request.user.is_authenticated:
        return redirect('')
    return render(request, 'employees.html',
        {'employees': Employee.objects.filter(user__id = request.user.id, status=True)})