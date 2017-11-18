from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
from music_store.models import Libruary
from django.core.paginator import Paginator


@csrf_exempt
def remove(request):
    track = {}
    if request.method == 'POST':
        new_track = Libruary(
            track_no = 1, 
            track_name = request.POST.get("track_name",""),
            artist = request.POST.get("artist",""), 
            album = 1,
            genre = 1)
        
        new_track.save()
        
        #track['track_name'] = request.POST.get("track_name","")
        #track['artist'] = request.POST.get("artist","")
        
        #cursor = connections['default'].cursor()
        
        #     "INSERT INTO libruary SET track_name = 'Baby', 
        #     artist = 'Biber'"
    
        #cursor.execute("INSERT INTO libruary SET track_name = '"  + \
        #track['track_name'] + "', artist = '" + track['track_name'] + "'")

    result = render(request, 'add.html', track)
    
    return result
