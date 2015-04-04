from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'yelpy.views.home'),
    url(r'^login/$', 'yelpy.views.auth'),
    url(r'^logout/$', 'yelpy.views.log_out'),
    url(r'^users/(?P<user_id>\w+)/$', 'yelpy.views.user_view'),
    url(r'^admin/', include(admin.site.urls)),
)
