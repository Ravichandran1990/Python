from django.urls import path
from .views import ArtistView, SongView
urlpatterns = [
    path('', ArtistView.as_view()), 
    path('song/', SongView.as_view())
]