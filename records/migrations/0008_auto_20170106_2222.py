# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_recentchanges'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecentChanges',
            new_name='RecentChange',
        ),
    ]
