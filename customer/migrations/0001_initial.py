# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('seller', models.ForeignKey(verbose_name='seller', to=settings.AUTH_USER_MODEL)),
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
                ('name', models.CharField(max_length=32)),
                ('birth', models.DateField()),
                ('gender', models.CharField(default=b'1', max_length=8, choices=[(1, '\u7537'), (2, '\u5973')])),
                ('addr', models.CharField(max_length=32)),
                ('phone', models.IntegerField()),
                ('Email', models.CharField(max_length=32)),
                ('QQ', models.IntegerField()),
                ('beizhu', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
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
                ('commission_sale_leader_sum', models.FloatField(verbose_name='commission sale leader sum')),
                ('commission_team_leader_sum', models.FloatField(verbose_name='commission team leader sum')),
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
                ('title', models.CharField(max_length=32)),
                ('start_time', models.DateField(default=datetime.datetime.now)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='xiaoshou',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(default=b'1', max_length=8, choices=[(1, '\u5143'), (2, '\u4e07\u5143')])),
                ('start_time', models.DateField(default=datetime.datetime.now)),
                ('end_time', models.DateField()),
                ('beizhu', models.CharField(max_length=256)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('xiaoshou', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='project_name',
            field=models.ForeignKey(verbose_name='project name', to='customer.Project'),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(verbose_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customer',
            name='project',
            field=models.ForeignKey(to='customer.Project'),
        ),
        migrations.AddField(
            model_name='customer',
            name='xiaoshourenyuan',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
