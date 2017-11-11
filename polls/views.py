from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from polls.models import Libruary
from django.core.paginator import Paginator

@csrf_exempt
def index(request):
    
    #cursor = connections['default'].cursor()
    #cursor.execute("SELECT " + \
    #        "libruary.track_no," + \
    #       "libruary.artist," + \
    #       "libruary.track_name," + \
    #       "genre.name AS genre_name" + \
    #   " FROM libruary" + \
    #   " LEFT JOIN genre ON (libruary.genre = genre.id)")
    
    rows = Libruary.objects.all()

    paginator = Paginator(rows, 2)
    # dictfetchall(cursor)
    page = request.GET.get('page', 1)
    p_rows = paginator.page(page)
    

    result = render_to_string('index.html', {
        'my_string': 'Dima',
        'track_rows': p_rows
    })
    
    return HttpResponse(result)





@csrf_exempt
def add(request):
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

    result = render_to_string('add.html', track)
    
    return HttpResponse(result)
@csrf_exempt
def edit(request):
    track = {}
    row = Libruary.objects.get(id=request.GET.get("id",1))

    if request.method == 'POST':
        row.track_name = request.POST.get("track_name","")
        row.artist = request.POST.get("artist","")
        row.save()

    track['row'] = row
    result = render_to_string('edit.html',track)

    return HttpResponse(result)






def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    