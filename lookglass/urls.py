from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin



urlpatterns = patterns(
    'lookglass.mk.views',
    url(r'^$', 'index', name='index'),
    url(r'^resultado/$', 'resultado', name='resultado'),
    # Examples:
    # url(r'^$', 'lookglass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Habilita index /off para media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

# Desabilita index /off para staticfiles    
urlpatterns += staticfiles_urlpatterns()