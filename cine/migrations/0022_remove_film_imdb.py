# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0021_cinephile_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='imdb',
        ),
    ]
