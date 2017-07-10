# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-06 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]