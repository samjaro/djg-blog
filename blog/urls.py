from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

    url(r'^post/new/$', views.post_new, name='post_new'),

    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^vitoria$', views.vitoria, name='vitoria'),

    #url(r'^vitoria/(?P<pk>[0-9]+)/$', views.vitoria_detail, name='vitoria_detail'),

    url(r'^florida', views.florida, name='florida'),

    url(r'^santa_maria', views.santa_maria, name='santa_maria'),

    url(r'^cuesta', views.cuesta, name='cuesta'),
    url(r'^contact', views.contact, name='contact'),
]
