# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150801_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='photo',
        ),
        migrations.AddField(
            model_name='places',
            name='text',
            field=models.TextField(default=datetime.datetime(2015, 8, 4, 1, 9, 1, 618794, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
