from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro

def VistaIndex(request):
    au = request.META.get('REMOTE_ADDR', 'unknown')
    #au = request.META['REMOTE_ADD']
    return HttpResponse('Tu navegador es: %s' % au)

def buscar(request):

    error = False

    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'biblioteca/resultados.html', {'libros':libros, 'query':q})

    return render(request, 'biblioteca/formulario_buscar.html', {'error':error})
