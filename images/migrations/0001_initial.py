# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-17 03:06
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('alt', models.CharField(default='', max_length=256)),
                ('date_posted', models.DateField(blank=True)),
                ('mature', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='')),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Ashton\\PycharmProjects\\Furryous\\media'), upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_posted',),
            },
        ),
    ]
