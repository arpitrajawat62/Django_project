from django.shortcuts import render, redirect
from core.models import Video
from core.forms import VideoForm

def home(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    
    videos = Video.objects.all().order_by('-id')
    context = {
        'form': form,
        'videos': videos,
    }
    return render(request, 'home.html', context)


