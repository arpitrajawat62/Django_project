from django.contrib import messages
from django.shortcuts import render
from .models import Video
from .utils import generate_transcript, generate_notes_from_transcript

def generate_notes(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        if not url:
            messages.error(request, "No URL provided.")
            return render(request, 'home.html')

        video = Video.objects.create(url=url)

        transcript, error = generate_transcript(video)

        if error:
            messages.error(request, f"Transcript error: {error}")
            return render(request, 'home.html')

        notes = generate_notes_from_transcript(transcript)
        video.notes = notes
        video.save()

        messages.success(request, "Notes generated successfully!")
        return render(request, 'home.html', {'video': video})  

    return render(request, 'home.html') 


def register(request):
    pass

def login(request):
    pass



