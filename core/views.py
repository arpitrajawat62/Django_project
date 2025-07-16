from rest_framework import status
from django.shortcuts import render, redirect
from .models import Video



def generate_notes(request):
    if request.method == 'POST':   
        url = request.POST.get('url')
        if url:
         Video.objects.create(url=url)
    return redirect('home')

def register(request):
    pass

def login(request):
    pass



