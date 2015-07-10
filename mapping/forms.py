from django import forms
# from django.contrib.auth.models import Group
from django.forms import  Textarea
from mapping.models import Country, Department, Task, Subtask, Description

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        exclude = []

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = []

        labels = {'name' : 'DEPARTMENT NAME'}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = []

        labels = {'name':'TASK NAME'}

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        exclude = []

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        exclude = ['created_at','subtask','country']

        widgets = {

            'description': Textarea(attrs={'class': 'materialize-textarea', 'required': True}),
        }

        labels = {'description' : 'TASK DESCRIPTION'}