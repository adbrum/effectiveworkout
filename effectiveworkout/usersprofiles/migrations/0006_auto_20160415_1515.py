# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import effectiveworkout.usersprofiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('usersprofiles', '0005_auto_20160415_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to=effectiveworkout.usersprofiles.models.user_directory_path),
        ),
    ]
