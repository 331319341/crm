# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_contract_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='project_name',
            field=models.ForeignKey(verbose_name='project name', to='customer.Project'),
        ),
    ]
