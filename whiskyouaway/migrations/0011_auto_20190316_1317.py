# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whiskyouaway', '0010_auto_20190316_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='fish',
            new_name='categories',
        ),
    ]
