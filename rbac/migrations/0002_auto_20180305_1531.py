# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-05 07:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='permission',
            new_name='permissions',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='role',
            new_name='roles',
        ),
    ]
