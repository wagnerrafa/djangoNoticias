from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def pagina1(request):

    return render(request, 'pagina1.html')
