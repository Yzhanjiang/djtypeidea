# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, '\u4e0a\u7ebf'), (3, '\u5220\u9664')], default=1, verbose_name='\u72b6\u6001'),
        ),
    ]
