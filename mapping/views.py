from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'mapping/home.html',{'title':'HOME'})

def department(request):
    return render(request,'mapping/departments.html',{'title':'DEPARTMENTS'})

def newframework(request):
    return render(request,'mapping/newframework.html',{'title':'NS in NEW FRAMEWORK'})

def nsd(request):
    return render(request,'mapping/nsd.html',{'title':'NATIONAL SOCIETY DEVELOPMENT'})

def youth(request):
    return render(request,'mapping/youth.html',{'title':'YOUTH'})

def volunteer(request):
    return render(request,'mapping/volunteer.html',{'title':'VOLUNTEERING'})
