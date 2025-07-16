from django.contrib import admin
from .models import Video
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import openai

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('url','processed','created_at','updated_at')
    actions = ['generate_transcript_and_notes']

    def extract_video_id(self,url):
        query = urlparse(url)
        video_id = parse_qs(query.query).get("v")
        return video_id[0] if video_id else None
    
    def generate_transcript(self,request,queryset):

    
admin.site.register(Video,VideoAdmin)