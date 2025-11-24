from django.urls import path
from .views import CategoryListView, BusinessListView, BusinessDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<str:slug>', BusinessListView.as_view(), name='business_list'),
    path('<str:slug>/', BusinessDetailView.as_view(), name='business_detail'),
]
