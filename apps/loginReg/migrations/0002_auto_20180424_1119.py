# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='email',
            new_name='emai',
        ),
    ]