from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
from music_store.models import Artists
from django.core.paginator import Paginator
import json as JSON

@csrf_exempt
def index(request):
    
    rows = Artists.objects.all()

    paginator = Paginator(rows, 2)
    # dictfetchall(cursor)
    page = request.GET.get('page', 1)
    p_rows = paginator.page(page)
    

    result = render(request, 'artists.html', {
        'artists': p_rows
    })
    
    return result

@csrf_exempt
def json(request):
    res = []
    
    rows = Artists.objects.filter(name__contains=request.GET.get('q', ''))
    for row in rows:
        res.append({'id':row.name, 'text':row.name}) 
    #result = render_to_string('artists_json.html', {
    #    'artists': p_rows
    #})
    result = JSON.dumps(res)
    return HttpResponse(result)