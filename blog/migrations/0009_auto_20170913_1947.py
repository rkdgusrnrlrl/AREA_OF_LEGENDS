# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170913_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='blog.Member'),
        ),
    ]
