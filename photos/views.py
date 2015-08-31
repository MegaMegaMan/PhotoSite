from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.context_processors import csrf
import datetime
from django.db.models import Count

from .models import Album,Photo,Comment

def albums(request):
	all_albums_list = Album.objects.order_by('album_name')
	context = {'all_albums_list': all_albums_list}
	return render(request, 'photos/albums.html', context)

def photos(request,album_id):
	all_photos_list = Photo.objects.filter(photo_album_id=album_id)
	comments = Photo.objects.annotate(comments_count=Count('comment__comment_photo_id'))
	context = {'all_photos_list': all_photos_list,'comments':comments}
	return render(request, 'photos/photos.html', context)	

def photo(request,photo_id):
	if request.POST:
		photo_comment = Comment()
		photo_comment.comment_user=request.POST.get('user_name')
		photo_comment.comment_text=request.POST.get('text')
		photo_comment.comment_photo_id = get_object_or_404(Photo, pk=photo_id).id
		photo_comment.comment_date = datetime.datetime.now()
		photo_comment.save()
	photos = get_object_or_404(Photo, pk=photo_id)
	comments_list = Comment.objects.filter(comment_photo_id=photos).order_by('-comment_date')
	context = {'photos':photos,'comments_list':comments_list}	
	context.update(csrf(request))
	return render(request, 'photos/photo.html', context)

	