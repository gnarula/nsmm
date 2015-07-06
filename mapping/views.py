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
    if request.method == "POST":
        form = DescriptionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.subtask = Subtask.objects.get(id=subtask)
            instance.user = request.user
            instance.country = request.user.country
            instance.save()
            return HttpResponseRedirect('/department/(?P<department>\d+)/task/(?P<task>\d+)/subtask/(?P<subtask>\d+)', {'success': 'Task Added'})
        else:
            return render(request, 'mapping/viewsubtask.html', {'form': form, 'title': 'Task'})
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
