from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
from music_store.models import Libruary
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from django.db.models import Q

@csrf_exempt
def index(request):
    search = request.GET.get("q","")
    if search != "":
        rows = Libruary.objects.filter(Q(track_name__contains=search) | Q(artist__contains=search))
    else:
        rows = Libruary.objects.all()

    paginator = Paginator(rows, 10)
    # dictfetchall(cursor)
    page = request.GET.get('page', 1)
    p_rows = paginator.page(page)
    

    result = render(request, 'index.html', {
        'my_string': 'Dima',
        'track_rows': p_rows,
        'auth': True, 
        'user1': request.user,
        'q' : search
    } )
    
    return result
