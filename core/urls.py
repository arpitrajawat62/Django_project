from django.urls import path
from . import views



urlpatterns = [
   
    path('generate_notes/', views.generate_notes, name='generate_notes'),

]
