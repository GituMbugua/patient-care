# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='deals_with',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='care.Department'),
        ),
    ]
