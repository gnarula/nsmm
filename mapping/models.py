from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self,
        username,
        first_name,
        last_name,
        country,
        password
    ):
        """
        Creates a new user
        """

        if not username:
            raise ValueError('User must have a username')

        c = Country.objects.get(pk=country)

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            country=c
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username,
        first_name,
        last_name,
        country,
        password
    ):
        """
        Creates a new superuser
        """


        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            country=country,
            password=password,
        )

        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    username = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    department = models.ForeignKey(Department)
    email = models.EmailField(unique=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'country',
    ]

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

    def is_filled(self, country):
        start = date(date.today().year, 1, 1)
        end = date(date.today().year, 12, 31)
        return Description.objects.filter(subtask=self, country__id=country, created_at__gte=start, created_at__lte=end).exists()

class Description(models.Model):
    STATUS = (
        (1, 'Not started'), # 45
        (2, 'Initial Stages'), # 43
        (3, 'Mostly Accomplished'), # 42
        (4, 'Complete'), # 49
    )

    subtask = models.ForeignKey(Subtask)
    country = models.ForeignKey(Country)
    created_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)
    status = models.IntegerField(choices=STATUS)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.subtask.__str__()
