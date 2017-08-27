# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 10:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170827_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='headline',
            field=models.CharField(max_length=200, verbose_name='titulo'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 7, 46, 29, 973164), help_text='For an entry to be published, it must be active and its publication date must be in the past.', verbose_name='fecha publicaci\xf3n'),
        ),
    ]