# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w_menu', '0003_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=256, unique=True, verbose_name='title'),
        ),
    ]
