from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def entry(request):
    return render(request, 'entry.html')

def klienten_list(request):
    klientinnen = Klienten.objects.all()
    ctx = {'klientinnen': klientinnen}
    return render(request, 'klienten_list.html', ctx)

def klienten_detail(request, id):
    klient = Klienten.objects.get(id = id)
    ctx = {'klient': klient}
    return render(request, 'klienten_detail.html', ctx)

def klienten_update(request):
    return render(request, 'klienten_update.html')
