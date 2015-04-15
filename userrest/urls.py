from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'userrest.views.home', name='home'),
    #url(r'^user/', include('logrest.urls', namespace="user")),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/', include('logrest.urls', namespace='user')),
    
    
)
