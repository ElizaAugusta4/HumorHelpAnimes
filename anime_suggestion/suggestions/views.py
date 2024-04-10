from django.shortcuts import render
from .models import Anime

def suggest_anime(request):
    humor = request.GET.get('humor', '')
    if humor:
        animes = Anime.objects.filter(humor__icontains=humor)
    else:
        animes = Anime.objects.all()
    return render(request, 'suggestions/anime_suggestions.html', {'animes': animes})
