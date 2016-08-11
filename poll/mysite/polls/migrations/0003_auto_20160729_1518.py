# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 19:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='use', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together=set([('user', 'votes')]),
        ),
    ]