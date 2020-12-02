from django.urls import path, include
from . import views

urlpatterns = [
    path('api/Actors/', views.all_actors)
]
