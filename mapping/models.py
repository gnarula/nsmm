from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    # add other fields/metadata here 
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    # add other fields/metadata here

    def __str__(self):
        return self.name  

class TaskDir(models.Model):
    country = models.ForeignKey(Country)
    department = models.ForeignKey(Department)
    task = models.CharField(max_length=100)
    subtask = models.CharField(max_length=100)    

    def __str__(self):
        return self.id

class TaskDesc(models.Model):
    STATUS = (
        (1, 'Not started'),
        (2, 'Initial Stages'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Complete'),
    )

    task_dir = models.ForeignKey(TaskDir)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return self.task_dir.subtask