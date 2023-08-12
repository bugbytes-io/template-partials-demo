from django.shortcuts import render
from core.forms import FilmForm
from core.models import Film

def index(request):
    context = {'form': FilmForm(), 'films': Film.objects.all()}
    return render(request, 'index.html', context)