from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'news/index.html', {})

def about(request):
    return render(request, 'news/about_us.html', {})
