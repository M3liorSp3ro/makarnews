from django.shortcuts import render, redirect
from .models import Task

def index(request):
    a = Task.objects.order_by('-pub_date')
    return render(request, 'news/index.html', {'a':a})

def about(request):
    return render(request, 'news/about_us.html', {})
