# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0008_auto_20171215_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(blank=True, max_length=50)),
                ('deals_with', models.ManyToManyField(blank=True, to='care.Cause')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.AddField(
            model_name='patient',
            name='cause',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='care.Cause'),
        ),
    ]
