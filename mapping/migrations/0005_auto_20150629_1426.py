# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0004_auto_20150625_0844'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='taskdesc',
            name='task_dir',
        ),
        migrations.RemoveField(
            model_name='taskdir',
            name='country',
        ),
        migrations.RemoveField(
            model_name='taskdir',
            name='department',
        ),
        migrations.DeleteModel(
            name='TaskDesc',
        ),
        migrations.DeleteModel(
            name='TaskDir',
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
    ]
