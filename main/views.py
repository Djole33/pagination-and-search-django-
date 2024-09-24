from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
    all_movies = Movies.objects.all()

    movie_name = request.GET.get('movie_name')
    
    if movie_name != '' and movie_name is not None:
        all_movies = all_movies.filter(name__icontains=movie_name)

    paginator = Paginator(all_movies, 4)
    page_number = request.GET.get('page')
    all_movies = paginator.get_page(page_number)

    return render(request, 'main/movie_list.html', {'all_movies': all_movies})
