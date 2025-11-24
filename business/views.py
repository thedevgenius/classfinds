from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Business
# Create your views here.
class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.filter(parent__isnull=True).prefetch_related('children').order_by('order')
        return render(request, 'business/categories.html', {'categories': categories})
    
class BusinessListView(View):
    def get(self, request, slug):
        # Placeholder for business listing logic
        category = get_object_or_404(Category, slug=slug)
        businesses = Business.objects.filter(categories=category)
        return render(request, 'business/business_list.html', {'category': category, 'businesses': businesses})

class BusinessDetailView(View):
    def get(self, request, slug):
        business = get_object_or_404(Business.objects.prefetch_related('attributes__type'), slug=slug)
        grouped = {}
        for attr in business.attributes.all():
            grouped.setdefault(attr.type, []).append(attr)
        return render(request, 'business/business_detail.html', {'biz': business, 'grouped_attributes': grouped})