# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-01 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=255),
        ),
    ]