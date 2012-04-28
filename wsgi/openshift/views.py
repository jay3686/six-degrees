import os
import pymongo
from django.shortcuts import render_to_response
from django.utils import simplejson
rom django.http import HttpResponse

connection = pymongo.Connection('mongodb://admin:4A5buhckPFSw@127.6.89.1:27017/')
#connection = pymongo.Connection('localhost', 27017)
db = connection.six

def home(request):
    return render_to_response('home/home.html')



def getActors(request):
    name = request.POST.get('name', False)

    adb = db.actors.find_one({"name":name})

    return HttpResponse(simplejson.dumps(adb), mimetype='application/javascript')
