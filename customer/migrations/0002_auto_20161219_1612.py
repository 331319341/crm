# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('birth', models.DateField()),
                ('addr', models.CharField(max_length=32)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=32)),
                ('qq', models.IntegerField()),
                ('beizhu', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='xiaoshou',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('beizhu', models.CharField(max_length=256)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('unit', models.ForeignKey(to='customer.Unit')),
                ('xiaoshou', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='reported_by',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.ForeignKey(to='customer.Gender'),
        ),
        migrations.AddField(
            model_name='customer',
            name='project',
            field=models.ForeignKey(to='customer.Project'),
        ),
        migrations.AddField(
            model_name='customer',
            name='shoumairen',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
