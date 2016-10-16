# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 17:12
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ec2-user/furryous/media'), upload_to='', verbose_name='Profile Picture'),
        ),
    ]
