import os, sys
import linecache

from django.db import models
from django.utils import timezone
from django.urls import reverse

# This is the structor of our post,
# necessarly for the SQL
class Post(models.Model):
	author = models.CharField(max_length=10, null=True)
	content = models.TextField(max_length = 1000)
	now_date = models.DateTimeField(default = timezone.now)

	def absolute_url(self):
		return reverse('post forum')