# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0004_auto_20171214_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]