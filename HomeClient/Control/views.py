from django.shortcuts import render
from Control.models import Lamp
from django.http import HttpResponse
# Create your views here.
def getLamps(request):
    return render(request,'index.html')

def getColor(request):
    col = request.GET['c']
    c=Lamp.objects.filter(color=col)
    return HttpResponse(str(c))
def addLamp(request):
    pin=request.GET['pin']
    loc=request.GET['location']
    col=request.GET['color']

    l=Lamp(pin=int(pin),location=loc,color=col)
    l.save()
    allLamps=Lamp.objects.all()
    return HttpResponse(allLamps)