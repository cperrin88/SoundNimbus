# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('actor_id', models.CharField(max_length=255)),
                ('object_id', models.CharField(max_length=255)),
                ('actor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Outbox',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('actor_id', models.CharField(max_length=255)),
                ('object_id', models.CharField(max_length=255)),
                ('actor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]