# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
