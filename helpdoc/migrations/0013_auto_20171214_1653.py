# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdoc', '0012_auto_20171213_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateField(),
        ),
    ]