from django.conf.urls import patterns, include, url
from jrbsite.views import hello, current_datetime, hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^hello/$', hello),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^admin/', include(admin.site.urls)),
)

