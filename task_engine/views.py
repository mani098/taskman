from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from forms import CreateTaskForm
from controllers import update_activity_feeds, get_activity_feeds, get_created_tasks, get_assigned_tasks

def login_view(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')
	else:
		if request.method == 'POST':
			email_id = request.POST.get('email_id')
			username = email_id.split('@')[0]
			password = request.POST.get('password')

			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect("/home/")
				else:
					return HttpResponse("Your taskman account is disabled.")
			else:
				return render(request, 'login.html', {'message': "invalid login"})
		else:
			return render(request, 'login.html', {})


@login_required
def home_view(request):
	current_user = request.user
	message = None
	activity_feeds = get_activity_feeds(request.user.id)
	if request.method == 'POST' and 'create-task-btn' in request.POST:
		create_task_form = CreateTaskForm(data=request.POST)
		if create_task_form.is_valid():
			task_form = create_task_form.save(commit=False)
			task_form.user_id = request.user.id
			task_form.save()
			message = "Task created successfully"
			task_name = request.POST.get('task_name')
			update_activity_feeds(request.user.id, task_name, "you created task ")
			activity_feeds = get_activity_feeds(request.user.id)

	return render(request, 'home.html', {'username': current_user.username, 'message': message,
										'activity_feeds': activity_feeds})

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def get_user_suggestions(request):
	user_name = request.GET.get('term')
	suggested_users = User.objects.filter(username__startswith=user_name).values_list('username', flat=True)
	return JsonResponse(list(suggested_users), safe=False)

@login_required
def created_tasks_view(request):
	user_id = request.user.id
	# return JsonResponse(get_created_tasks(user_id), safe=False)
	return render(request, 'created_tasks.html', {'tasks': get_created_tasks(user_id)})

@login_required
def assigned_tasks_view(request):
	user_id = request.user.id

	return render(request, 'assgined_tasks.html', {'tasks': get_assigned_tasks})