# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-24 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProTwo', '0004_userprofileinfo_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
