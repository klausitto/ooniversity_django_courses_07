# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170525_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]