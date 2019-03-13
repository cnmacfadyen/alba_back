# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-13 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whiskyouaway', '0005_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertText', models.CharField(max_length=200)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiskyouaway.Event')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='CategoryContainer',
        ),
    ]