# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180602_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='completion_date',
            field=models.DateField(),
        ),
    ]
