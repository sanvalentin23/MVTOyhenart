from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime 
from MVTOyhenart.models import Familiar

def saludo(request):
    return HttpResponse("Hola Django - coder")


def obtenerfamiliares(self):
    familiares = Familiar.objects.all()
    
    diccionario =  {"familiares":familiares}

    miHtml = open("C:/Users/PC/Desktop/Proyecto django/MVTOyhenart/MVTOyhenart/templates/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def guardarfamiliares(self):
    familiar1= Familiar(nombre="Silvina", edad=53, nacimiento="1969-05-08")
    familiar2 = Familiar(nombre="Tino", edad=52, nacimiento="1970-05-26")
    familiar3 = Familiar(nombre="Luciano", edad=21, nacimiento="2000-10-23")
    familiar1.save()
    familiar2.save()
    familiar3.save()

    return HttpResponse("familiares guardados")

def obtenerfamiliar(self, nombrefamiliar):
    familiares = Familiar.objects.filter(nombre=nombrefamiliar)

    diccionario =  {"familiares":familiares}

    miHtml = open("C:/Users/PC/Desktop/Proyecto django/MVTOyhenart/MVTOyhenart/templates/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)


