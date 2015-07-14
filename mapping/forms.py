from django import forms
# from django.contrib.auth.models import Group
from django.forms import Textarea, SelectMultiple, PasswordInput
from mapping.models import Country, CustomUser, Department, Task, Subtask, Description
from django.contrib.auth.hashers import make_password

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
        exclude = ['department']

        labels = {
            'department': 'DEPARTMENT NAME' ,
            'name': 'TASK NAME'
        }

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        exclude = ['task']

        labels = {
            'name': 'SUBTASK NAME' ,
            'task': 'TASK NAME'
        }

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        exclude = ['created_at','subtask','country']

        widgets = {
            'description': Textarea(attrs={'class': 'materialize-textarea', 'required': True}),
        }

        labels = {'description' : 'TASK DESCRIPTION'}

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = []

        widgets = {
            'password': PasswordInput()
        }

    def save(self, commit=True):
        instance = super(UserForm, self).save(commit=False)

        if commit:
            instance.password = make_password(self.cleaned_data['password'])
            instance.save()
            self.save_m2m()

        return instance

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['password']
