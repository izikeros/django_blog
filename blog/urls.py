from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='name_post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='name_post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='name_post_edit'),
    url(r'^post/new/$', views.post_new, name='name_post_new'),
]