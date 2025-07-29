from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Video
from core.utils import generate_transcript, generate_notes_from_transcript

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        if not url:
            messages.error(request, "No URL provided.")
            return redirect('home')

        video = Video.objects.create(url=url)

        transcript, error = generate_transcript(video)

        if error:
            messages.error(request, f"Transcript error: {error}")
            return redirect('home')

        notes = generate_notes_from_transcript(transcript)
        video.notes = notes
        video.processed = True
        video.save()

        messages.success(request, "Notes generated successfully!")
        return redirect('home')

    # GET request - display all videos
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'videos': videos})



