# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0005_auto_20180424_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='birthday',
        ),
    ]
