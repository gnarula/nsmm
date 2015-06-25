# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0002_auto_20150619_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdesc',
            name='status',
            field=models.IntegerField(choices=[(1, 'Not started'), (2, 'Initial Stages'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Complete')]),
        ),
        migrations.AlterField(
            model_name='taskdir',
            name='department',
            field=models.CharField(max_length=2, choices=[('HE', 'Health'), ('OD', 'Organisation Development'), ('DM', 'Disaster Management')]),
        ),
    ]
