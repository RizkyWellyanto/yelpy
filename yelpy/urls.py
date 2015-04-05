from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'yelpy.views.home'),
    url(r'^welcome/$', 'yelpy.views.welcome'),

    url(r'^login/$', 'yelpy.views.auth'),
    url(r'^logout/$', 'yelpy.views.log_out'),
    url(r'^register/$', 'yelpy.views.register'),

    url(r'^search_user/$', 'yelpy.views.search_user'),

    url(r'^users/(?P<user_id>\w+)/$', 'yelpy.views.user_view'),
    url(r'^users/(?P<user_id>\w+)/create_comment/$', 'yelpy.views.create_comment'),

    url(r'^admin/', include(admin.site.urls)),
)
