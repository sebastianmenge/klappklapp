from django.conf.urls import patterns, include, url


urlpatterns = patterns('marcador.views',
    url(r'^user/(?P<username>[-\w]+)/$', 'bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^$', 'bookmark_list', name='marcador_bookmark_list'),
)
