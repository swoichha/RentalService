# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-07 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0010_auto_20180207_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='tag',
        ),
    ]
