from rest_framework import serializers
from api.models import Card
from django.shortcuts import render
from . models import Card
from .seializers import CardSerializeer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        card_no = request.POST['card_no']
        expiry = request.POST['expiry']
        cvv = request.POST['cvv']
        card = Card(name = name, card_no= card_no, expiry = expiry, cvv = cvv)
        card.save()
    return render(request, 'index.html')





def card_detail(request, ck):
    card = Card.objects.get(id = ck)
    serializer = CardSerializeer(card)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type= 'application/json')

def card_list(request):
    card = Card.objects.all()
    serializer = CardSerializeer(card, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type= 'application/json')
