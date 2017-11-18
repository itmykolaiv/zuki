from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
from music_store.models import Artists
from django.core.paginator import Paginator


@csrf_exempt
def edit(request):
    
    artist = Artists.objects.get(id=request.GET.get("id","0"))
    if request.method == 'POST':
        artist.name = request.POST.get("name","")
        artist.description = request.POST.get("description","")
        artist.save()
        
    result = render(request, 'edit_artist.html', {'artist':artist})
    
    return result

@csrf_exempt
def view(request):
    
    artist = Artists.objects.get(name=request.GET.get("name","0"))
    result = render(request, 'view_artist.html', {'artist':artist})
    
    return result
