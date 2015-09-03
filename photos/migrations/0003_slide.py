# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150901_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('slide_photo', models.ImageField(upload_to=photos.models.Slide.getAlbum)),
            ],
        ),
    ]
