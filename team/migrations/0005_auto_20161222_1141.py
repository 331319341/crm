# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20161222_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_leader',
            field=models.IntegerField(blank=True, max_length=32, null=True, verbose_name='team name', choices=[(3L, '1212'), (2L, 'hello'), (1L, '\u674e\u6587\u9f99')]),
        ),
    ]
