# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskies', '0006_auto_20160503_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagsearch',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]