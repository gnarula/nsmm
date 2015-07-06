from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from mapping.forms import CountryForm, DepartmentForm, TaskForm, SubtaskForm, DescriptionForm
from mapping.models import Country, Department, Task, Subtask, Description
from django.template import Library

# Create your views here.

register = Library

def home(request):
    return render(request,'mapping/home.html',{'title':'HOME'})

def login(request):
    # if user is logged in then redirect to the dashboard
    if request.user.is_authenticated():
        return HttpResponseRedirect('/department')

    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print(password)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None and user.is_active:
            # Login the user
            auth.login(request, user)
            return JsonResponse({'message': 'Login Successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid Username/Password'}, status=500)
    return render(request, 'mapping/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')

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
