from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'task_engine.views.login_view', name='login'),  # index page
	url(r'^', include('task_engine.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
