# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-08 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20180307_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='permissiongroup',
            name='parent',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.PermissionGroup'),
        ),
    ]
