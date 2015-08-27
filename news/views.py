from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import News

def news(request,news_id):
	news = get_object_or_404(News, pk=news_id)
	return render(request, 'news/news.html', {'news': news})

def news_list(request):
	all_news_list = News.objects.order_by('-news_date')
	context = {'all_news_list': all_news_list}
	return render(request, 'news/news_list.html', context)