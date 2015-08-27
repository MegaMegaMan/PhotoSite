# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('album_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('comment_text', models.CharField(max_length=400)),
                ('comment_date', models.DateTimeField(verbose_name='date published')),
                ('comment_user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('photo_description', models.CharField(max_length=400)),
                ('photo_link', models.ImageField(upload_to=models.ForeignKey(to='photos.Album'))),
                ('photo_album', models.ForeignKey(to='photos.Album')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_photo',
            field=models.ForeignKey(to='photos.Photo'),
        ),
    ]
