# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
