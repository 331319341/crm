# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20161222_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_leader',
            field=models.IntegerField(blank=True, null=True, verbose_name='team name', choices=[(3L, '1212'), (2L, 'hello'), (1L, '\u674e\u6587\u9f99')]),
        ),
    ]
