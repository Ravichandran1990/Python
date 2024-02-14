from django.urls import path, include
from .views import ProductViews, ProductStatusView

urlpatterns = [    
    path('', ProductViews.as_view()),
    path('status/', ProductStatusView.as_view())
]
