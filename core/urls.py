from django.urls import path
from . import views
from views import *


urlpatterns = [
   
    path('generate_notes/', views.generate_notes, name='generate_notes'),
    path('api/submit-video/',submit_video, name='submit_video'),

    # path('generate_transcript/', views.generate_transcript, name='generate_transcript'),
   
]
