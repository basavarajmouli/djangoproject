# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140704_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.CharField(default=b'Author', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.CharField(default=b'Sports', max_length=100),
            preserve_default=True,
        ),
    ]
