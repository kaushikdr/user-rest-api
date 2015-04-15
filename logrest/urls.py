from django.conf.urls import patterns, url
from logrest import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
	url(r'^$', views.UserList.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^signup/$', views.signup, name ='signup'),
	url(r'^login/$', views.LoginView.as_view()),
	url(r'^logout/$', views.logout, name ='logout'),
	#url(r'^signup', include(router.urls)),

	)

urlpatterns = format_suffix_patterns(urlpatterns)