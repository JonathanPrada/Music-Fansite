from django.conf.urls import url
from . import views


# Namespace for our music app
app_name = 'music'


# Registered URLs
urlpatterns = [
    # /music/
    # Convert the Index class to a view
    url(r'^$', views.IndexView.as_view(), name='index'),


    # /music/register/
    # Place to register a new user
    url(r'^register/$', views.UserFormView.as_view(), name='register'),


    # /music/<album_id>/
    # Convert the Detail class to a view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),


    # /music/album/add (no pk as it is a new album)
    # Assigned to model form
    url(r'album/add/$', views.AlbumCreate.as_view(), name="album-add"),


    # /music/album/2/
    # Assigned to model form delete
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album-update"),


    # /music/album/2/delete
    # Assigned to model form
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="album-delete"),
]
