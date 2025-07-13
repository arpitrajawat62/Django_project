from django.shortcuts import render, redirect
from django.http import JsonResponse
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from core.models import Video
from core.forms import VideoForm



def home(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            return redirect('home')
      
    else:
      form = VideoForm()
      
    videos = Video.objects.all().order_by('-id')
    context = {
            'form': form,
            'videos': videos,
    }
    return render(request, 'home.html', context)

def generate_trancript(request):
    if request.method == "POST":
         Video_url = request.POST.get("video_url")
  
         query = urlparse(Video_url)
         video_id = parse_qs(query.query).get("v")
  
         if not video_id:
             return JsonResponse({"error":"invalid YouTube URL"})
         
         video_id = video_id[0]
      
      try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([x['text']for x in transcript_list])


