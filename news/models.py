from django.db import models

class News(models.Model):
	def __str__(self):
		return self.news_text
	news_date = models.DateTimeField('date published')
	news_text = models.CharField(max_length=800)
