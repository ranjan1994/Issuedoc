# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-22 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdoc', '0018_auto_20171220_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='tag3',
            field=models.CharField(default='Human', max_length=50),
            preserve_default=False,
        ),
    ]
