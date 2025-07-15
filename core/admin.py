from django.contrib import admin
from .models import Video
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import openai

# Register your models here.

admin.site.register(Video)

