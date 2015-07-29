from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^login/$', views.login_view, name='login'),
	url(r'^home/', views.home_view, name='home'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^get-users/', views.get_user_suggestions, name='get_suggested_users'),
	url(r'^created-tasks/', views.created_tasks_view, name='created-tasks'),
	url(r'^assigned-tasks/', views.assigned_tasks_view, name='assigned-tasks'),
	)
