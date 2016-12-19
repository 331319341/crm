# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20161219_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xiaoshou',
            name='unit',
            field=models.CharField(default=b'1', max_length=8, choices=[(1, b'\xe5\x85\x83'), (2, b'\xe4\xb8\x87\xe5\x85\x83')]),
        ),
    ]
