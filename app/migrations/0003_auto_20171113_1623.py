# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 18:23
from __future__ import unicode_literals

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171113_1550'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', app.models.UsuarioManager()),
            ],
        ),
    ]
