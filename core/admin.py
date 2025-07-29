from django.contrib import admin
from .models import Video
from .utils import generate_transcript

class VideoAdmin(admin.ModelAdmin):
    list_display = ('pk','url','processed','created_at')
    actions = ['generate_notes_from_transcript']

    def generate_transcript(self, request, queryset):
        for video in queryset:
            generate_transcript(video)
        self.message_user(request, "Transcript generation completed.")

    generate_transcript.short_description = "Generate Transcript Only"

admin.site.register(Video, VideoAdmin)