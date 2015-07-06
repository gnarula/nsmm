from django.conf.urls import patterns, include, url
from django.contrib import admin
from mapping import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nsmm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home),
    url(r'^department$',views.department),
    url(r'^department/(?P<department>\d+)/task/(?P<task>\d+)$',views.tasks),
    url(r'^department/(?P<department>\d+)/task/(?P<task>\d+)/subtask/(?P<subtask>\d+)$',views.subtasks),
    url(r'^od/newframework$',views.newframework),
    url(r'^od/nsd$',views.nsd),
    url(r'^od/youth$',views.youth),
    url(r'^od/volunteer$',views.volunteer),
)
