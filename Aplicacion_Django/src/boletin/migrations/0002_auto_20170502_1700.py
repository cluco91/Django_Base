# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrado',
            name='codigo_postal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
