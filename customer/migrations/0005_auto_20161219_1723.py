# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20161219_1637'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
        migrations.AddField(
            model_name='customer',
            name='begin',
            field=models.DateField(null=True, verbose_name='begin date', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='creator', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='end',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='modification',
            field=models.DateTimeField(auto_now=True, verbose_name='modification', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='modifier',
            field=models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='begin',
            field=models.DateField(null=True, verbose_name='begin date', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='creator', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='end',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='modification',
            field=models.DateTimeField(auto_now=True, verbose_name='modification', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='modifier',
            field=models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='begin',
            field=models.DateField(null=True, verbose_name='begin date', blank=True),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='creator', blank=True),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='end',
            field=models.DateField(null=True, verbose_name='end date', blank=True),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='modification',
            field=models.DateTimeField(auto_now=True, verbose_name='modification', null=True),
        ),
        migrations.AddField(
            model_name='xiaoshou',
            name='modifier',
            field=models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True),
        ),
    ]
