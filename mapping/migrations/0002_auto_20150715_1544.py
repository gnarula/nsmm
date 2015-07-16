# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(null=True, to='mapping.Department'),
        ),
    ]
