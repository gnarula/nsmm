from django.shortcuts import render
from mapping.forms import CountryForm, DepartmentForm, TaskForm, SubtaskForm, DescriptionForm
from mapping.models import Country, Department, Task, Subtask, Description
from django.template import Library

# Create your views here.

register = Library

def home(request):
    return render(request,'mapping/home.html',{'title':'HOME'})

def department(request):
    departments = Department.objects.all().order_by('name')
    d = Department()
    tasks = Task.objects.all().order_by('name')
    t = Task()
    # total_depts = sum(0 == 0 for department in departments)
    # total_tasks = sum(0 == 0 for task in tasks)
    return render(request,'mapping/departments.html',{'departments': departments, 'title':'Departments', 'tasks': tasks})

def tasks(request, department=None, task=None):
    department = Department.objects.get(id=department)
    task = Task.objects.get(id=task)
    d = department.id
    t = task.id
    departments = Department.objects.all().order_by('name')
    tasks = Task.objects.all().order_by('name')
    subtasks = Subtask.objects.all().order_by('name')
    return render(request,'mapping/viewtask.html',{'tasks' : tasks, 'departments': departments, 'subtasks': subtasks, 'd' : d, 't' : t})

def subtasks(request, department=None, task=None, subtask=None):
    # department = Department.objects.get(id=department)
    # task = Task.objects.get(id=task)
    # d = department.id
    # t = task.id
    # departments = Department.objects.all().order_by('name')
    # tasks = Task.objects.all().order_by('name')
    # subtasks = Subtask.objects.all().order_by('name')
    # return render(request,'mapping/viewtask.html',{'tasks' : tasks, 'departments': departments, 'subtasks': subtasks, 'd' : d, 't' : t})
    pass

def newframework(request):
    return render(request,'mapping/newframework.html',{'title':'NS in NEW FRAMEWORK'})

def nsd(request):
    return render(request,'mapping/nsd.html',{'title':'NATIONAL SOCIETY DEVELOPMENT'})

def youth(request):
    return render(request,'mapping/youth.html',{'title':'YOUTH'})

def volunteer(request):
    return render(request,'mapping/volunteer.html',{'title':'VOLUNTEERING'})
