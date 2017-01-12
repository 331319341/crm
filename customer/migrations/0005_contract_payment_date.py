# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_project_cata'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='payment_date',
            field=models.DateField(default=b'2017-01-12', verbose_name='payment date'),
        ),
    ]
