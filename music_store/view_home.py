from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
from music_store.models import Libruary
from django.core.paginator import Paginator
from django.contrib.auth import authenticate


@csrf_exempt
def index(request):

    cursor = connections['default'].cursor()
    cursor.execute("""SELECT 
           libruary.artist,
           libruary.track_name,
           libruary.embed 
           FROM libruary 
           ORDER BY RANDOM() LIMIT 3
           """)
    
    rows = dictfetchall(cursor)
    
    result = render(request, 'home.html', {'rows': rows})
    
    return result

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
