# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 18:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20171113_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Curso')),
            ],
            options={
                'abstract': False,
            },
            bases=('app.usuario',),
        ),
    ]