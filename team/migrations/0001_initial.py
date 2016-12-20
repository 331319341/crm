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
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('passwd', models.CharField(max_length=32, verbose_name='passwd')),
                ('create_time', models.DateField(verbose_name='create time')),
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
                ('name', models.CharField(max_length=32, verbose_name='team name')),
                ('create_time', models.DateField(verbose_name='create time')),
                ('team_leader', models.CharField(max_length=32, verbose_name='team name')),
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
            field=models.ForeignKey(verbose_name='project name', to='team.Team'),
        ),
    ]
