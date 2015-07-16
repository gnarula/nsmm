# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.EmailField(null=True, unique=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=500)),
                ('status', models.IntegerField(choices=[(1, 'Not started'), (2, 'Initial Stages'), (3, 'Mostly Accomplished'), (4, 'Complete')])),
                ('country', models.ForeignKey(to='mapping.Country')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(to='mapping.Department')),
            ],
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(to='mapping.Task'),
        ),
        migrations.AddField(
            model_name='description',
            name='subtask',
            field=models.ForeignKey(to='mapping.Subtask'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.ForeignKey(to='mapping.Country'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(to='mapping.Department'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_query_name='user', blank=True, verbose_name='groups', related_name='user_set'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', blank=True, verbose_name='user permissions', related_name='user_set'),
        ),
    ]
