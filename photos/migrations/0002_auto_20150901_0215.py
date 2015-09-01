# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_photo',
            field=models.ImageField(upload_to=photos.models.Album.getAlbum, default=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_link',
            field=models.ImageField(upload_to=photos.models.Photo.getAlbum),
        ),
    ]
