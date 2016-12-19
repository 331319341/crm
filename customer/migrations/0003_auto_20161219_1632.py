# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20161219_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(default=b'1', max_length=2, verbose_name='gender', choices=[('0', '\u672a\u77e5\u7684\u6027\u522b'), ('1', '\u7537\u6027'), ('2', '\u5973\u6027'), ('9', '\u672a\u8bf4\u660e\u7684\u6027\u522b')]),
        ),
    ]
