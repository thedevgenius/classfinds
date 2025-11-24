from django.urls import path
from .views import CategoryListView, BusinessListView, BusinessDetailView, LocationSelectView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('select-location/', LocationSelectView.as_view(), name='location_select'),
    path('category/<str:slug>', BusinessListView.as_view(), name='business_list'),
    path('<str:slug>/', BusinessDetailView.as_view(), name='business_detail'),
    
]
