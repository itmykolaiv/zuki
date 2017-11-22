from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from music_store.models import Artists
from django.core.paginator import Paginator


@csrf_exempt
def add(request):
    artist = {}
    if request.method == 'POST':
        artist = Artists(
            name = request.POST.get("name",""),
            description = request.POST.get("description","")
        )
        artist.save()
    result = render(request, 'add_artist.html', {'artist':artist})
    
    return result

@csrf_exempt
def delete(request):
    artist = Artists.objects.get(id=request.GET.get("id","0"))
    if request.method == 'POST' and request.POST.get('confirm') == "1":
        artist = Artists.objects.get(id=request.POST.get("id","0"))
        artist.delete()
        return redirect("/artists/")
    result = render(request, 'delete_artist.html', {'artist':artist})
    
    return result

