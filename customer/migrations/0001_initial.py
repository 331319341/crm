# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=32, verbose_name='number')),
                ('into_way', models.CharField(max_length=32, verbose_name='into way')),
                ('project_name', models.CharField(max_length=32, verbose_name='project name')),
                ('customer_name', models.CharField(max_length=32, verbose_name='customer name')),
                ('customer_ID', models.CharField(max_length=32, verbose_name='customer ID')),
                ('bank_name', models.CharField(max_length=32, verbose_name='bank name')),
                ('bank_account', models.CharField(max_length=32, verbose_name='bank account')),
                ('buy_date', models.DateField(verbose_name='buy date')),
                ('buy_sum', models.IntegerField(verbose_name='buy sum')),
                ('buy_category', models.CharField(max_length=32, verbose_name='buy category')),
                ('buy_deadline', models.IntegerField(verbose_name='buy deadline')),
                ('year_rate', models.FloatField(verbose_name='year rate')),
                ('seller', models.ForeignKey(verbose_name='seller', to='team.Employee')),
            ],
            options={
                'verbose_name': 'sale contract',
                'verbose_name_plural': 'sale contracts',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateField(null=True, verbose_name='begin date', blank=True)),
                ('end', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('creator', models.CharField(max_length=20, null=True, verbose_name='creator', blank=True)),
                ('modifier', models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True)),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True)),
                ('modification', models.DateTimeField(auto_now=True, verbose_name='modification', null=True)),
                ('name', models.CharField(max_length=32, verbose_name='customer name')),
                ('birth', models.DateField(verbose_name='customer birth')),
                ('gender', models.CharField(default=b'1', max_length=8, verbose_name='customer gender', choices=[(b'1', '\u7537'), (b'2', '\u5973')])),
                ('addr', models.CharField(max_length=32, verbose_name='customer addr')),
                ('phone', models.IntegerField(verbose_name='phone')),
                ('Email', models.CharField(max_length=32, verbose_name='Email')),
                ('QQ', models.IntegerField(verbose_name='QQ')),
                ('beizhu', models.CharField(max_length=256, verbose_name='beizhu')),
            ],
            options={
                'verbose_name': 'sale customer',
                'verbose_name_plural': 'sale customers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sale_leader', models.CharField(max_length=32, verbose_name='sale leader')),
                ('team_leader', models.CharField(max_length=32, verbose_name='team leader')),
                ('customer_name', models.CharField(max_length=32, verbose_name='customer name')),
                ('start_time', models.DateField(default=datetime.datetime.now, verbose_name='start time')),
                ('buy_sum', models.IntegerField(verbose_name='buy sum')),
                ('buy_deadline', models.IntegerField(verbose_name='buy deadline')),
                ('year_rate', models.FloatField(verbose_name='year rate')),
                ('commission_sale_leader', models.CharField(max_length=32, verbose_name='commission sale leader')),
                ('commission_team_leader', models.CharField(max_length=32, verbose_name='commission team leader')),
                ('commission_sale_leader_rate', models.FloatField(verbose_name='commission sale leader rate')),
                ('commission_team_leader_rate', models.FloatField(verbose_name='commission team leader rate')),
                ('commission_sale_leader_sum', models.FloatField(null=True, verbose_name='commission sale leader sum')),
                ('commission_team_leader_sum', models.FloatField(null=True, verbose_name='commission team leader sum')),
                ('commission_deadline', models.IntegerField(verbose_name='commission deadline')),
                ('manager', models.CharField(max_length=32, verbose_name='manager')),
            ],
            options={
                'verbose_name': 'sale order',
                'verbose_name_plural': 'sale orders',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.DateField(null=True, verbose_name='begin date', blank=True)),
                ('end', models.DateField(null=True, verbose_name='end date', blank=True)),
                ('creator', models.CharField(max_length=20, null=True, verbose_name='creator', blank=True)),
                ('modifier', models.CharField(max_length=20, null=True, verbose_name='modifier', blank=True)),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='creation', null=True)),
                ('modification', models.DateTimeField(auto_now=True, verbose_name='modification', null=True)),
                ('title', models.CharField(max_length=32, verbose_name='project name')),
                ('start_time', models.DateField(default=datetime.datetime.now, verbose_name='start time')),
                ('description', models.CharField(max_length=256, null=True, verbose_name='project desc')),
            ],
            options={
                'verbose_name': 'sale project',
                'verbose_name_plural': 'sale projects',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='project_name',
            field=models.ForeignKey(verbose_name='project name', to='customer.Project'),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(verbose_name='seller', to='team.Employee'),
        ),
        migrations.AddField(
            model_name='customer',
            name='project',
            field=models.ForeignKey(verbose_name='project name', to='customer.Project'),
        ),
        migrations.AddField(
            model_name='customer',
            name='seller',
            field=models.ForeignKey(verbose_name='seller', to='team.Employee'),
        ),
    ]
