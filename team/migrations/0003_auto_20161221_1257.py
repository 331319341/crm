# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20161221_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='begin',
            field=models.DateField(null=True, verbose_name='begin date', blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='creator', blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='end',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='modification',
            field=models.DateTimeField(auto_now=True, verbose_name='modification', null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='modifier',
            field=models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(verbose_name='project team', to='team.Team'),
        ),
    ]
