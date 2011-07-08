import sys
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.shortcuts import redirect

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^i18n/', include('django.conf.urls.i18n')),   
    #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #url(r'^feinheit/', include('feinheit.urls')),
    
    url('^ajax/(?P<path>.*)/', 'screen.views.random_content'),
)

#urlpatterns += patterns('django.views.generic.simple',
    #url(r'^$', lambda request: redirect('/%s/' % short_language_code())),
    #url(r'^$', 'direct_to_template', {'template': 'home.html'}),
    #url(r'^$', 'redirect_to', {'url': '/where/do/you/want/to/go/today/'}),
#)

if 'runserver' in sys.argv:
    urlpatterns += patterns('',
#        url('^(.*).manifest$', 'views.serve_manifest'),
    )

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )

    urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'', include('feincms.urls')),
)
