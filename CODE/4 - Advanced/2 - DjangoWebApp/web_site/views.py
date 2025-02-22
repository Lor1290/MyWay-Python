from django.shortcuts import render
from django.http import HttpResponse
from .models import Post # -> import database post


### dummy data post ###
posts = [
    {
        'author': 'Lorenzo Poli',
        'title': 'Test Post 1',
        'content': 'test_web_site',
        'date': '24/08/2024'
    },
    {
        'author': 'Lorenzo Cagnin',
        'title': 'Test Post 2',
        'content': 'test_web_site',
        'date': '24/08/2025'
    }
]

### dummy data about ###
about = [
    {
        'author': 'Lorenzo Poli',
        'title': 'Test Post 1',
        'content': 'test_web_site',
        'date': '24/08/2024'
    },
    {
        'author': 'Lorenzo Cagnin',
        'title': 'Test Post 2',
        'content': 'test_web_site',
        'date': '24/08/2025'
    }
]

class Pages:
    global context
    context = {
        'posts':  Post.objects.all(), #-> importa interamente i dati in base ai nomi da noi dati.
        'about': 'about',
        'home_tile':  'home page', 
        'about_title': 'about page' 
    }
    
    def home(request):
        return render(request, 'web_site/home.html', context)
    
    def about(request):
        return render(request, 'web_site/about.html', context)
    def email_page(request):
        return HttpResponse("<h1>Start of the about link page</h1>")

    def link(request):
        return HttpResponse("<h1>Start of the link page</h1>")

