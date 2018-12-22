# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-19 20:29
from __future__ import unicode_literals

import app.models.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_interface', models.CharField(default=b'', max_length=30)),
                ('remote_interface', models.CharField(default=b'', max_length=30, null=True)),
                ('status', models.CharField(choices=[(app.models.models.Status(b'Down'), b'Down'), (app.models.models.Status(b'Shutdown'), b'Shutdown'), (app.models.models.Status(b'Up'), b'Up')], default=app.models.models.Status(b'Down'), max_length=50)),
                ('connected_interface', models.CharField(default=b'', max_length=30)),
                ('connected_router', models.CharField(default=b'', max_length=30)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='models.Card')),
            ],
        ),
    ]