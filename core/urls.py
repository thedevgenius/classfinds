from django.urls import path
from .views import HomeView, LocationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('location/', LocationView.as_view(), name='location'),
]
