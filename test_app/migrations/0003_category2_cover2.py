# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20160505_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='category2',
            name='cover2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.Cover'),
        ),
    ]
