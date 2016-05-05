# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', filebrowser.fields.FileBrowseField(default='/files/assets/images/placeholder.jpg', max_length=200, verbose_name='Image')),
            ],
        ),
        migrations.RemoveField(
            model_name='category2',
            name='cover2',
        ),
    ]