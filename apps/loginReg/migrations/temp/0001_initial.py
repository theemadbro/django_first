# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=55)),
                ('fname', models.CharField(max_length=22)),
                ('lname', models.CharField(max_length=22)),
                ('password', models.CharField(max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]