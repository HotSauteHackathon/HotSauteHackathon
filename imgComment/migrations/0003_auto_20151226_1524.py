# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgComment', '0002_auto_20151226_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='url',
            new_name='imageUrl',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='postTag',
            new_name='postUrl',
        ),
        migrations.AddField(
            model_name='image',
            name='content',
            field=models.CharField(default='None', max_length=300),
        ),
    ]
