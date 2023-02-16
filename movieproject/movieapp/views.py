from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movie_form
from .models import movies


# Create your views here.
def index(request):
    obj = movies.objects.all()
    context = {
        'movie': obj
    }
    return render(request, 'index.html', context)

def details(request, movie_id):
    movie = movies.objects.get(id=movie_id)

    return render(request, 'details.html', {'m':movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year = request.POST.get('year')
        price = request.POST.get('price')
        img = request.FILES['img']

        new_movie = movies(name=name, year=year, price=price, img=img)
        new_movie.save()
        return redirect('/')

    return render(request, 'Add.html')

def update(request, id):

    movie = movies.objects.get(id=id)
    form = movie_form(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'form':form, 'movie':movie})

def delete(request, id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'del.html')