# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.Photo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.Photo'),
            preserve_default=False,
        ),
    ]
