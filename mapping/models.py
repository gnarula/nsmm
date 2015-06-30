from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    department = models.ForeignKey(Department)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{0}::{1}".format(self.department, self.name)

class Subtask(models.Model):
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{0}::{1}".format(self.task, self.name)

class Description(models.Model):
    STATUS = (
        (1, 'Not started'),
        (2, 'Initial Stages'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Complete'),
    )

    subtask = models.ForeignKey(Subtask)
    country = models.ForeignKey(Country)
    created_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)
    status = models.IntegerField(choices=STATUS)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return "{0}::{1}".format(self.task, self.name)
