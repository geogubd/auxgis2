# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 17:13
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0004_recordnameedit_recordpositionedit'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordShapeEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.gis.db.models.fields.GeometryCollectionField(srid=4326, verbose_name='data')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('attrib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.AttributeType')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
