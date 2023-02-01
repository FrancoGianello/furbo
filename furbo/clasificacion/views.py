from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def clasificacion(request):
    return HttpResponse("Esta es la clasificacion")