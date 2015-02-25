from django.conf.urls import patterns, include, url
from django.contrib import admin

from pics import views as pics_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'serve.views.home', name='home'),
    url(r'^7kreator$', 'seven_kreator.views.home'),
    url(r'^pics/', include('pics.urls', namespace='rooming')),
    url(r'^admin/', include(admin.site.urls)),
)
