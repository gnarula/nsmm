from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from datetime import date
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
    departments = Department.objects.all().order_by('name')
    tasks = Task.objects.all().order_by('name')
    subtasks = Subtask.objects.filter(task=task).order_by('name')
    title = Task.objects.get(id=task).name
    return render(request,'mapping/viewtask.html',{'subtasks': subtasks ,'title': title ,'departments': departments, 'tasks': tasks})

def subtasks(request, department=None, task=None, subtask=None):
    departments = Department.objects.all().order_by('name')
    tasks = Task.objects.all().order_by('name')
    subtasks = Subtask.objects.filter(task=task).order_by('name')
    title = Task.objects.get(id=task).name
    try:
        description = Description.objects.get(subtask=subtask)
        date_created = description.created_at.year
        date_today = date.today().year
        if date_today != date_created:
            description = None
    except Description.DoesNotExist:
        description = None
    if request.method == "POST":
        if description:
            form = DescriptionForm(request.POST, instance=description)
        else:
            form = DescriptionForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.subtask = Subtask.objects.get(id=subtask)
            instance.user = request.user
            instance.country = request.user.country
            instance.save()
            dest_url = '/department/{0}/task/{1}/subtask/{2}'.format(department, task, subtask)
            return HttpResponseRedirect(dest_url, {'success': 'Task Added', 'subtasks': subtasks ,'title': title, 'departments': departments, 'tasks': tasks , 'form': form})
        else:
            return render(request, 'mapping/viewsubtask.html', {'form': form, 'title': 'Task'})
    else:
        if description:
            form = DescriptionForm(instance=description)
        else:
            form = DescriptionForm()
        return render(request,'mapping/viewsubtask.html',{'subtasks': subtasks ,'title': title ,'departments': departments, 'tasks': tasks , 'form':form })

def newframework(request):
    return render(request,'mapping/newframework.html',{'title':'NS in NEW FRAMEWORK'})

def nsd(request):
    return render(request,'mapping/nsd.html',{'title':'NATIONAL SOCIETY DEVELOPMENT'})

def youth(request):
    return render(request,'mapping/youth.html',{'title':'YOUTH'})

def volunteer(request):
    return render(request,'mapping/volunteer.html',{'title':'VOLUNTEERING'})
