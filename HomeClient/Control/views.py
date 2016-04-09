from django.shortcuts import render
from Control.models import Lamp
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from Arduino.controller import *

def main(request):
    return render(request,'index.html')

def changePin(request):
    pin = request.GET['pin']
    val = request.GET['val']
    pin = int(pin)
    val = int(val)

    c.changePin(pin,val)
    if val == 0:
        return HttpResponse("Pin {} is now {}".format(pin,"on"))

    if val == 1:
        return HttpResponse("Pin {} is now {}".format(pin, "off"))


def allLamps(request):
    pins=[]
    for pin in c._pins:
        pins.append({'pin' : pin,'val': c._pins[pin]._value})
    return JsonResponse(pins, safe=False)

def addLamp(request):
    pin=request.GET['pin']
    loc=request.GET['location']
    col=request.GET['color']

    l=Lamp(pin=int(pin),location=loc,color=col)
    l.save()