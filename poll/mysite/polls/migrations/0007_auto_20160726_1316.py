# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160726_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seu',
            name='user',
        ),
        migrations.DeleteModel(
            name='seu',
        ),
    ]
