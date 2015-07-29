from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from forms import CreateTaskForm


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
	if request.method == 'POST' and 'create-task-btn' in request.POST:
		create_task_form = CreateTaskForm(data=request.POST)
		if create_task_form.is_valid():
			create_task_form.save()
			message = "Task created successfully"
	return render(request, 'home.html', {'username': current_user.username, 'message': message})

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def get_user_suggestions(request):
	user_name = request.GET.get('term')
	suggested_users = User.objects.filter(username__startswith=user_name).values_list('username', flat=True)
	return JsonResponse(list(suggested_users), safe=False)