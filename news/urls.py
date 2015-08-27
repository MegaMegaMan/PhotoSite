from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^/news_list/$',views.news_list, name='news_list'),
    	url(r'^(?P<news_id>[0-9]+)/$', views.news, name='news'),
    ]  