from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from music_store.models import Libruary
from django.core.paginator import Paginator


@csrf_exempt
def add(request):
    track = {}
    track['row'] = {}
    if request.method == 'POST':
        new_track = Libruary(
            track_no = 1, 
            track_name = request.POST.get("track_name",""),
            artist = request.POST.get("artist",""), 
            album = request.POST.get("album",""),
            genre = request.POST.get("genre",""),
            embed = request.POST.get("embed","")
        )
        track['row'] = new_track
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

@csrf_exempt
def delete(request):
    track = Libruary.objects.get(id=request.GET.get("id","0"))
    if request.method == 'POST' and request.POST.get('confirm') == "1":
        track = Libruary.objects.get(id=request.POST.get("id","0"))
        track.delete()
        return redirect("/tracks/")
    result = render(request, 'delete.html', {'track':track})
    
    return result

