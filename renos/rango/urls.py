from django.conf.urls import patterns, url
from rango import views
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), 
    )
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    