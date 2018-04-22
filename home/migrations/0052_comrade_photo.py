# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-20 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_roundpage_internapproval'),
    ]

    operations = [
        migrations.AddField(
            model_name='comrade',
            name='photo',
            field=models.ImageField(blank=True, upload_to=home.models.make_comrade_photo_filename),
        ),
    ]