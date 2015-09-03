from django.db import models
from time import localtime,strftime

class Album(models.Model):
	def __str__(self):
		return self.album_name
	def getAlbum(instance, filename):
		return  '%s/%s' % (instance.album_name,'cover-' + strftime("%d%m%Y-%H:%M:%S"))	
	album_name = models.CharField(max_length=100)
	album_photo = models.ImageField(upload_to=getAlbum)

class Photo(models.Model):
	def getAlbum(instance, filename):
		return  '%s/%s' % (instance.photo_album.album_name, strftime("%d%m%Y-%H:%M:%S"))
	photo_album = models.ForeignKey(Album)
	photo_description = models.CharField(max_length=400, blank=True)
	photo_link = models.ImageField(upload_to=getAlbum)
	
class Comment(models.Model):
	comment_photo = models.ForeignKey(Photo)
	comment_text = models.CharField(max_length=400)
	comment_date = models.DateTimeField('date published')
	comment_user = models.CharField(max_length=30)

class Slide(models.Model):
	def getAlbum(instance, filename):
		return  '%s/%s' % ('Slides','slide-' + strftime("%d%m%Y-%H:%M:%S"))
	slide_photo = models.ImageField(upload_to=getAlbum)			

