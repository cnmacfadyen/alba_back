# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 11:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertText', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('image', models.ImageField(upload_to='static/categories_images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
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
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiskyouaway.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='Admin', max_length=128)),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.CharField(max_length=9999, null=True)),
                ('avgRating', models.FloatField(null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='events_images')),
                ('url', models.URLField(max_length=128)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiskyouaway.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writtenReview', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiskyouaway.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', multiselectfield.db.fields.MultiSelectField(choices=[('Music', 'Music'), ('Animals', 'Animals'), ('Nightlife', 'Nightlife'), ('Sport', 'Sport'), ('Outdoors', 'Outdoors'), ('History', 'History'), ('Family', 'Family'), ('Food and Drink', 'Food and Drink')], max_length=68)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
