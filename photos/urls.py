from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^/albums/$',views.albums, name='albums'),
    	url(r'^albums/(?P<album_id>[0-9]+)/$', views.photos, name='photos'),
    	url(r'^photo/(?P<photo_id>[0-9]+)/$', views.photo, name='photo'),
    ] 