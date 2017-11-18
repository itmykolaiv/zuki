from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
from music_store.models import Libruary
from music_store.models import Artists
from django.core.paginator import Paginator

@csrf_exempt
def edit(request):
    track = {}
    row = Libruary.objects.get(id=request.GET.get("id","0"))
    track['row'] = row
    if request.method == 'POST':
        
        row.track_name = request.POST.get("track_name","")
        row.artist = request.POST.get("artist","")
        row.embed = request.POST.get("embed","")
        row.save()
        
    result = render(request, 'edit.html', track)
    
    return result

@csrf_exempt
def view(request):
    row = Libruary.objects.get(id=request.GET.get("id","0"))
    result = render(request, 'view.html', {'row': row})
    return result