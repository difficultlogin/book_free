# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 18:33
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('cover', filebrowser.fields.FileBrowseField(max_length=200, verbose_name='Image')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('desc', tinymce.models.HTMLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('slug2', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name')),
            ],
        ),
    ]
