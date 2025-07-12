from django.shortcuts import render, redirect
from .models import Video


def generate_notes(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        Video.objects.create(url=url)
    return redirect('home')

def register(request):
    # if request.method == 'POST':
    pass

def login(request):
    pass



