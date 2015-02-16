from django.conf.urls import patterns, include, url
from django.contrib import admin

from pics import views as pics_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'admin7k.views.home', name='home'),
    url(r'^pics/', include('pics.urls', namespace='rooming')),
    url(r'^admin/', include(admin.site.urls)),
)
