# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20160802_1523'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Roast',
        ),
    ]