# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-17 01:24
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161017_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Ashton\\PycharmProjects\\Furryous\\media'), upload_to='', verbose_name='Profile Picture'),
        ),
    ]