from django.conf.urls import url
from . import view_add_track
from . import view_tracks
from . import view_edit_track
from . import view_remove_track

urlpatterns = [
    url(r'^$', view_tracks.index, name='index'),
    url(r'^add$', view_add_track.add, name='add'),
    url(r'^delete$', view_add_track.delete, name='delete'),
    url(r'^edit$', view_edit_track.edit, name='edit'),
    url(r'^view$', view_edit_track.view, name='view'),
    url(r'^remove$', view_remove_track.remove, name='remove'),
]