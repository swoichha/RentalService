# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-29 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_auto_20180127_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='negotiable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rent',
            field=models.BigIntegerField(default=0),
        ),
    ]