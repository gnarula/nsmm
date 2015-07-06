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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=500)),
                ('status', models.IntegerField(choices=[(1, 'Not started'), (2, 'Initial Stages'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Complete')])),
                ('country', models.ForeignKey(to='mapping.Country')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
            name='groups',
            field=models.ManyToManyField(to='auth.Group', related_query_name='user', related_name='user_set', blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', related_query_name='user', related_name='user_set', blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.'),
        ),
    ]
