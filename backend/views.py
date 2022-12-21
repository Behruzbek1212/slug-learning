from django.shortcuts import render
from .models import *

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)

def about(request, slug):
    posts = Post.objects.get(slug=slug)
    context = {
        'posts': posts
    }

    return render(request, 'about.html', context)
