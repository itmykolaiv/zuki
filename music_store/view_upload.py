from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string
from django.shortcuts import render
from music_store.models import Libruary
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
import json as JSON
from django.conf import settings

@csrf_exempt
def index(request):
    result = {}
    if request.FILES['file'].name != "":
        handle_uploaded_file(request.FILES['file'])
        result = {'default': settings.STATIC_URL + 'upload/' + request.FILES['file'].name}
    return HttpResponse(JSON.dumps(result))
    
def handle_uploaded_file(f):
    with open(settings.BASE_DIR + settings.STATIC_URL + 'upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)