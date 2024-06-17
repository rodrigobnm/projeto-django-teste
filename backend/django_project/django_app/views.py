from django.shortcuts import render
from django.http import HttpResponse

dicionario_lista = [
    {
        'usuario': 'rodrigo',
        'idade': '17',
        'estagio': 'sim'
    },
    {
        'usuario': 'joao',
        'idade': '19',
        'estagio': 'nao'
    }
]

def home(request):
    geral = {
        'posts': dicionario_lista
    }
    return render(request, 'app/home.html', geral)

def sobre(request):
    return render(request, 'app/sobre.html')

def aba1(request):
    return render(request, "app/aba1.html")