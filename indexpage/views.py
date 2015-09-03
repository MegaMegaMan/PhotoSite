from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from news.models import News
from photos.models import Slide


def index(request):
	latest_news_list = News.objects.order_by('-news_date')[:5]
	slides = Slide.objects.all()
	context = {'latest_news_list': latest_news_list,'slides':slides}
	return render(request, 'indexpage/index.html', context)
    