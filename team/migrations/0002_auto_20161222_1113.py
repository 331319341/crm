# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(verbose_name='project team', to='team.Team', null=True),
        ),
    ]
