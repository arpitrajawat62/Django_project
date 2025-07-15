from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Video
from .serializers import VideoSerializer


def generate_notes(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        Video.objects.create(url=url)
    return redirect('home')

@api_view(['POST'])
def submit_video(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Video URL submitted succesfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

def register(request):
    # if request.method == 'POST':
    pass

def login(request):
    pass



