# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_entry_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='avatar',
        ),
        migrations.AddField(
            model_name='entry',
            name='image1',
            field=models.ImageField(default=2, help_text=b'50x180px image', upload_to=b'images/beerthumbs/'),
            preserve_default=False,
        ),
    ]
