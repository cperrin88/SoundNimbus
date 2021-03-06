# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='posts/files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Video'), (1, 'Audio'), (2, 'Picture')], null=True),
        ),
    ]
