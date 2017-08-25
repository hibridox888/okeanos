# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 07:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 25, 4, 19, 15, 353407), help_text='For an entry to be published, it must be active and its publication date must be in the past.', verbose_name='publication date'),
        ),
    ]