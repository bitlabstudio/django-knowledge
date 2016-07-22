from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.knowledge_index, name='knowledge_index'),

    url(r'^questions/$', views.knowledge_list, name='knowledge_list'),

    url(r'^questions/(?P<question_id>\d+)/$',
        views.knowledge_thread, name='knowledge_thread_no_slug'),

    url(r'^questions/(?P<category_slug>[a-z0-9-_]+)/$', views.knowledge_list,
        name='knowledge_list_category'),

    url(r'^questions/(?P<question_id>\d+)/(?P<slug>[a-z0-9-_]+)/$',
        views.knowledge_thread, name='knowledge_thread'),

    url(r'^moderate/(?P<model>[a-z]+)/'
        r'(?P<lookup_id>\d+)/(?P<mod>[a-zA-Z0-9_]+)/$',
        views.knowledge_moderate, name='knowledge_moderate'),

    url(r'^ask/$', views.knowledge_ask, name='knowledge_ask'),
]
