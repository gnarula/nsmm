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
        email,
        first_name,
        last_name,
        country,
        password
    ):
        """
        Creates a new user
        """

        if not email:
            raise ValueError('User must have a valid email address')

        c = Country.objects.get(pk=country)

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            country=c
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        first_name,
        last_name,
        country,
        password
    ):
        """
        Creates a new superuser
        """


        user = self.create_user(
            email=email,
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
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
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
