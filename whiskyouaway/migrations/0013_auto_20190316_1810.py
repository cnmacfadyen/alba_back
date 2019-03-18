# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whiskyouaway', '0012_auto_20190316_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', multiselectfield.db.fields.MultiSelectField(choices=[('Music', 'Music'), ('Animals', 'Animals'), ('Nightlife', 'Nightlife'), ('Sport', 'Sport'), ('Outdoors', 'Outdoors'), ('History', 'History'), ('Family', 'Family'), ('Food and Drink', 'Food and Drink')], max_length=68)),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='writtenReview',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(upload_to='events_images'),
        ),
        migrations.AlterField(
            model_name='review',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiskyouaway.Event'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
