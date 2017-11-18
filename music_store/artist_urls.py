from django.conf.urls import url

from . import view_add_artist
from . import view_artists
from . import view_edit_artist
from . import view_remove_artist

urlpatterns = [
    url(r'^$', view_artists.index, name='index'),
    url(r'^add$', view_add_artist.add, name='add'),
    url(r'^edit$', view_edit_artist.edit, name='edit'),
    url(r'^view$', view_edit_artist.view, name='edit'),
    url(r'^remove$', view_remove_artist.remove, name='remove'),
    url(r'^json$', view_artists.json, name='json'),
]