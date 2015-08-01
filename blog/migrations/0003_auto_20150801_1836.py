# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='places',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
