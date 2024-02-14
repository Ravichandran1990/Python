from django.urls import path
from .views import MovieViews, MovieDetailsViews
urlpatterns = [
    path('', MovieViews.as_view()),
    path('<int:pk>/', MovieDetailsViews.as_view()),
]