from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def topic_insert(request):
    WER = Topicform()
    d = {'WER': WER}
    if request.method == 'POST':
        abc = Topicform(request.POST)
        if abc.is_valid():
            abc.save()
            return HttpResponse('created')
        else:
            return HttpResponse('not created')
    return render(request,'topic_insert.html',d)
def insert_webpage(request):
    RTY = Webpageforms()
    d = {'RTY': RTY}
    if request.method == 'POST':
        asd = Webpageforms(request.POST)
        if asd.is_valid():
            asd.save()
            return HttpResponse('inserted')
        else:
            return HttpResponse('not inserted')
    return render(request,'insert_webpage.html',d)
