# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateField(null=True, verbose_name='begin date', blank=True)),
                ('end', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('creator', models.CharField(max_length=20, null=True, verbose_name='creator', blank=True)),
                ('modifier', models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True)),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True)),
                ('modification', models.DateTimeField(auto_now=True, verbose_name='modification', null=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='name')),
                ('passwd', models.CharField(max_length=32, verbose_name='passwd')),
                ('enter_date', models.DateField(verbose_name='enter date')),
            ],
            options={
                'verbose_name': 'sale employee',
                'verbose_name_plural': 'sale employees',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateField(null=True, verbose_name='begin date', blank=True)),
                ('end', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('creator', models.CharField(max_length=20, null=True, verbose_name='creator', blank=True)),
                ('modifier', models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True)),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True)),
                ('modification', models.DateTimeField(auto_now=True, verbose_name='modification', null=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='team name')),
                ('create_time', models.DateField(verbose_name='create time')),
                ('team_leader', models.IntegerField(null=True, verbose_name='leader name', blank=True)),
                ('description', models.CharField(max_length=256, null=True, verbose_name='team desc')),
            ],
            options={
                'verbose_name': 'sale team',
                'verbose_name_plural': 'sale teams',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(verbose_name='project team', blank=True, to='team.Team', null=True),
        ),
    ]
