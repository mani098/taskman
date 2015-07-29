from models import ActivityFeed, TaskVault


def update_activity_feeds(user_id, task_name, feed_type):
	"""Updates the activity_feeds of current user in ActivityFeed table"""

	feed = ActivityFeed(user_id=user_id, feed_name = feed_type+ task_name)
	feed.save()

def get_activity_feeds(user_id):
	"""Get all the activity_feeds of the current user"""

	activity_feeds = ActivityFeed.objects.filter(user_id=user_id).values_list('feed_name', flat=True)
	return list(activity_feeds)

def get_created_tasks(user_id):
	"""Returns all the tasks created by the user"""

	tasks = TaskVault.objects.filter(user_id=user_id).values('task_name', 'deadline_date', 'assignee')
	return list(tasks)

def get_assigned_tasks(user_id):

	tasks = TaskVault.objects.filter(user_id=user_id).values('task_name', 'deadline_date', 'username')
	return list(tasks)