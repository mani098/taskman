from django.db import models
from django.contrib.auth.models import User

class TaskVault(models.Model):

	user = models.ForeignKey(User, null=True)

	task_name = models.CharField(max_length=100)
	deadline_date = models.DateField(auto_now=False)
	assignee = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.task_name
