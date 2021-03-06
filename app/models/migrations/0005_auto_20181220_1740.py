# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_auto_20181220_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='router',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='models.Router'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interface', to='models.Card'),
        ),
    ]
