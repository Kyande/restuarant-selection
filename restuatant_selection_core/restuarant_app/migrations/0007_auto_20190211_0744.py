# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-11 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant_app', '0006_restaurant_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
