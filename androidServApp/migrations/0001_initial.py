# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-09 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('designation', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=128)),
                ('company', models.CharField(max_length=128)),
                ('ismanager', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1000)),
                ('startDate', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEmployeeRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='androidServApp.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='androidServApp.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManagerRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='androidServApp.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='androidServApp.Project')),
            ],
        ),
    ]