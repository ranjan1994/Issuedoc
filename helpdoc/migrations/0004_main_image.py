# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-30 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdoc', '0003_auto_20171129_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='image',
            field=models.ImageField(default=100, upload_to='media/image/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
