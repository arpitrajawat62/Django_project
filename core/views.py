from django.shortcuts import render, redirect
from .models import Video
from .utils import generate_transcript


def generate_notes(request):
    if request.method == 'POST':   
        url = request.POST.get('url')
        
        transcript = generate_transcript(url)
        Video.objects.create(url=url, transcript=transcript)
    return redirect('home')

def register(request):
    pass

def login(request):
    pass



