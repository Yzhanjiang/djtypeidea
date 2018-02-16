# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('href', models.URLField(verbose_name='\u94fe\u63a5')),
                ('status', models.PositiveIntegerField(choices=[(1, '\u6b63\u5e38'), (2, '\u5220\u9664')], default=1, verbose_name='\u72b6\u6001')),
                ('weight', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='\u6743\u91cd\u8d8a\u9ad8\u5c55\u793a\u987a\u5e8f\u7ea6\u9760\u524d', verbose_name='\u6743\u91cd')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
            ],
            options={
                'verbose_name': '\u53cb\u94fe',
                'verbose_name_plural': '\u53cb\u94fe',
            },
        ),
    ]