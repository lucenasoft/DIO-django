from django.shortcuts import render
from .models import Evento

# Create your views here.

def lista_eventos(request):
    evento = Evento.objects.all()
    return render(request,'evento.html', context= {
        'eventos': evento,
    })