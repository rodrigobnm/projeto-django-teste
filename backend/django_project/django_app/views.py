from django.shortcuts import render

dicionario_lista = [
    {
        'usuario': 'rodrigo',
        'idade': '17',
        'estagio': 'sim'
    },
    {
        'usuario': 'joao',
        'idade': '19',
        'estagio:': 'nao'
    }
]

def home(request):
    geral = {
        'posts': dicionario_lista
    }
    return render(request, 'app/home.html', geral)

def sobre(request):
    return render(request, 'app/sobre.html')