# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaskDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('status', models.IntegerField(choices=[(1, 'not started'), (2, 'initial stages'), (3, 'intermediate'), (4, 'advanced'), (5, 'complete')])),
            ],
        ),
        migrations.CreateModel(
            name='TaskDir',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('department', models.CharField(choices=[('Health', 'H'), ('Organisation Development', 'OD'), ('Disaster Management', 'DM')], max_length=40)),
                ('task', models.CharField(max_length=100)),
                ('subtask', models.CharField(max_length=100)),
                ('country', models.ForeignKey(to='mapping.Country')),
            ],
        ),
        migrations.AddField(
            model_name='taskdesc',
            name='task_dir',
            field=models.ForeignKey(to='mapping.TaskDir'),
        ),
    ]
