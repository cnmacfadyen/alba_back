# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whiskyouaway', '0003_events_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='username',
        ),
        migrations.RemoveField(
            model_name='review',
            name='writtenReview',
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.CharField(default='Admin', max_length=128),
        ),
        migrations.AlterField(
            model_name='review',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiskyouaway.Events'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, default=5),
        ),
    ]
