# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0004_auto_20171109_1531'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rhesis',
            unique_together=set([('poem_title', 'content')]),
        ),
    ]