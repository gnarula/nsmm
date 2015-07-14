from django.conf.urls import patterns, include, url
from django.contrib import admin
from mapping import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nsmm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home),
    url(r'^login$',views.login),
    url(r'^logout$', views.logout),
    url(r'^department$',views.department),
    url(r'^department/(?P<department>\d+)/task/(?P<task>\d+)$',views.tasks),
    url(r'^department/(?P<department>\d+)/task/(?P<task>\d+)/subtask/(?P<subtask>\d+)$',views.subtasks),
    url(r'^newdepartment$',views.newdepartment),
    url(r'^newtask$',views.newtask),
    url(r'^newsubtask$',views.newsubtask),
    url(r'^admin/filter$',views.filter),
    url(r'^admin/user$', views.user),
    url(r'^admin/user/new$',views.newuser),
    url(r'^admin/user/(?P<id>\d+)/edit$',views.edituser),
    url(r'^admin/department$', views.listdepartment),
    url(r'^admin/department/new$',views.newdepartment),
    url(r'^admin/department/(?P<id>\d+)/edit$',views.editdepartment),
    url(r'^admin/department/(?P<id>\d+)/task$',views.listtask),
    url(r'^admin/department/(?P<id>\d+)/task/new$',views.newtask),
    url(r'^admin/department/(?P<department>\d+)/task/(?P<task>\d+)/edit$',views.edittask),
    url(r'^admin/department/(?P<department_id>\d+)/task/(?P<task_id>\d+)/subtask$',views.listsubtask),
    url(r'^admin/department/(?P<department_id>\d+)/task/(?P<task_id>\d+)/subtask/new$',views.newsubtask),
    url(r'^admin/department/(?P<department_id>\d+)/task/(?P<task_id>\d+)/subtask/(?P<subtask_id>\d+)/edit$',views.editsubtask),
)
