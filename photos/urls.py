# photos/urls.py
from django.conf.urls import url

from . import views


app_name = 'photos'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.view_photo, name='view_photo'),
    url(r'^(?P<pk>[0-9]+)/like/$', views.like_photo, name='like_photo'),
    url(r'^create/$',views.create_photo, name="create_photo" ),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.delete_photo, name='delete_photo'),
    url(r'^add/comment/$',views.add_comment),
    url(r'^delete/comment/$',views.delete_comment),
    url(r'^$', views.toppage, name='toppage'),
]

