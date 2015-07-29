from django.db import models
from django.contrib.auth.models import User

class TaskVault(models.Model):

	user = models.ForeignKey(User)

	task_name = models.CharField(max_length=100)
	deadline_date = models.DateField(auto_now=False)
	assignee = models.CharField(max_length=50)

	def __unicode__(self):
		return self.task_name

class ActivityFeed(models.Model):

	user = models.ForeignKey(User)

	feed_name = models.CharField(max_length=150)

	def __unicode__(self):
		return self.feed_name