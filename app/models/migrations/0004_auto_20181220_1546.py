# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_remove_interface_connected_interface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='connected_router',
            field=models.CharField(default=b'', max_length=30, null=True),
        ),
    ]
