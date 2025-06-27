from django.shortcuts import render
from .models import Experiencia, Projeto

def home(request):
    experiencias = Experiencia.objects.all()
    projetos = Projeto.objects.all()
    return render(request, 'core/home.html', {
        'experiencias': experiencias,
        'projetos': projetos
    })
