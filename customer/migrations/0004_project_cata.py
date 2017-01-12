# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20170110_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cata',
            field=models.CharField(default=b'1', max_length=32, verbose_name='project cata', choices=[(b'1', '\u57fa\u91d1\u9879\u76ee'), (b'2', '\u501f\u6b3e\u9879\u76ee')]),
        ),
    ]
