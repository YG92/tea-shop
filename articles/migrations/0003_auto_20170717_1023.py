# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20170717_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]