from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()

    return render(request, "index.html", {'movie_list': movie})


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie1': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
        return redirect('/')
    return render(request, "add.html")


def update(request, id2):
    movie = Movie.objects.get(id=id2)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form': form, 'movie': movie})


def delete(request, id1):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id1)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")
