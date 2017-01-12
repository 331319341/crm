# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20170110_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='QQ',
            field=models.CharField(max_length=16, verbose_name='QQ'),
        ),
    ]
