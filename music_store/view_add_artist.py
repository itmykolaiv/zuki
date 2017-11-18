from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
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

