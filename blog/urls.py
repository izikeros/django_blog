from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='name_post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailVew.as_view(), name='name_post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.UpdatePostView.as_view(), name='name_post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.DeletePostView.as_view(), name='name_post_delete'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='name_post_new')

]