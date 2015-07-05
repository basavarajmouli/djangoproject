# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150628_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='bodyfull',
            field=models.TextField(default=datetime.datetime(2015, 6, 28, 17, 0, 5, 114000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
