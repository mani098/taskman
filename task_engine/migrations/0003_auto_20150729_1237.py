# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_engine', '0002_auto_20150729_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskvault',
            name='assignee',
            field=models.CharField(max_length=50),
        ),
    ]
