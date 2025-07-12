from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.URLField(help_text="Paste the YouTube video URL") 
    notes = models.TextField(blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False),
    error_message = models.BooleanField(default=False),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.task
