from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category
# Create your views here.
class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.filter(parent__id=1).order_by('name')
        return render(request, 'business/categories.html', {'categories': categories})
    
class BusinessListView(View):
    def get(self, request, slug):
        # Placeholder for business listing logic
        category = get_object_or_404(Category, slug=slug)
        return render(request, 'business/business_list.html', {'category': category})