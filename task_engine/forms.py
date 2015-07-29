from django import forms
from models import TaskVault


class CreateTaskForm(forms.ModelForm):
	class Meta:
		model = TaskVault
		fields = ('task_name', 'deadline_date', 'assignee')
