# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20161222_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(verbose_name='project team', blank=True, to='team.Team', null=True),
        ),
    ]
