# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdesc',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='taskdir',
            name='department',
            field=models.CharField(choices=[('HE', 'Health'), ('OD', 'Organisation Development'), ('DM', 'Disaster Management')], max_length=40),
        ),
    ]
