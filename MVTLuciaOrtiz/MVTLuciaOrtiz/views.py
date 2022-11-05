from django.http import HttpResponse
from django.template import loader
from Familiares.models import Familiares
from datetime import datetime

def inicio(request):
    familiar1 = Familiares(nombre= 'Lucia Ortiz', dni= 43281651, nacimiento= datetime(1997, 2, 12))
    familiar1.save()
    familiar2 = Familiares(nombre= 'Franco Muzzio', dni= 40009479, nacimiento= datetime(1997, 1, 24))
    familiar2.save()
    familiar3 = Familiares(nombre= 'Lucca Muzzio', dni= 66666665, nacimiento= datetime(2020, 2, 5))
    familiar3.save()
    lista_familiares = [familiar1,familiar2,familiar3]
    plantilla = loader.get_template('templates.html')
    contexto = {'lista_familiares': lista_familiares}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)