# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-08 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0002_profile_intrested_count")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="reviews_count",
            field=models.IntegerField(default=0),
        )
    ]
