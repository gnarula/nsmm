from django.shortcuts import render
from mapping.forms import CountryForm, DepartmentForm, TaskForm, SubtaskForm, DescriptionForm
from mapping.models import Country, Department, Task, Subtask, Description
# Create your views here.

def od(request):
    return render(request,'mapping/od.html',{'title':'User'})

def newframework(request):
    return render(request,'mapping/newframework.html',{'title':'NS in New Framework'})

def nsd(request):
    return render(request,'mapping/nsd.html',{'title':'National Society Development'})

def youth(request):
    return render(request,'mapping/youth.html',{'title':'YOUTH'})

def volunteer(request):
    return render(request,'mapping/volunteer.html',{'title':'VOLUNTEERING'})
