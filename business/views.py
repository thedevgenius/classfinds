from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db import models
from django.views import View
from .models import Category, Business, Location, Fecility
import json
from django.db.models import FloatField
from django.db.models.functions import ACos, Cos, Radians, Sin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pygeohash as pgh
# Create your views here.
class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.filter(parent__isnull=True).prefetch_related('children').order_by('order')
        return render(request, 'business/categories.html', {'categories': categories})
    
class BusinessListView(View):
    def get(self, request, slug):
        location = request.GET.get('location')
        print("Location from GET:", location)
        
        # Placeholder for business listing logic
        category = get_object_or_404(Category, slug=slug)
        businesses = Business.objects.filter(categories=category)
        return render(request, 'business/business_list.html', {'category': category, 'businesses': businesses})
    
    def post(self, request, slug):
        location_id = request.POST.get('location_id')
        location = get_object_or_404(Location, id=location_id)
        # Placeholder for business listing logic
        category = get_object_or_404(Category, slug=slug)
        businesses = Business.objects.filter(categories=category, locations=location)
        return render(request, 'business/business_list.html', {'category': category, 'businesses': businesses})

class BusinessDetailView(View):
    def get(self, request, slug):
        business = get_object_or_404(Business.objects.prefetch_related('attributes__type'), slug=slug)
        grouped = {}
        for attr in business.attributes.all():
            grouped.setdefault(attr.type, []).append(attr)
        fecilities = Fecility.objects.filter(business=business)
        return render(request, 'business/business_detail.html', {'biz': business, 'grouped_attributes': grouped, 'fecilities': fecilities})
    
# @method_decorator(csrf_exempt, name='dispatch')
class LocationSelectView(View):
    def get(self, request):
        location_id = request.GET.get('location_id')
        location = Location.objects.filter(id=location_id).first()
        return JsonResponse({
            "status": "success" if location else "not_found",
            "name": location.name if location else None,
            "geohash": location.geohash if location else None, 
            "nearest_city": location.city.name if location and location.city else None,
        })

    # def post(self, request):
    #     data = json.loads(request.body.decode("utf-8"))
    #     user_lat = float(data.get("lat"))
    #     user_lng = float(data.get("lng"))

    #     # Haversine formula (in meters)
    #     earth_radius = 6371000  # meters

    #     nearest = (
    #         Location.objects
    #         .filter(lat__isnull=False, lng__isnull=False)
    #         .annotate(
    #             distance=
    #                 earth_radius * ACos(
    #                     Cos(Radians(models.F("lat"), output_field=FloatField())) *
    #                     Cos(Radians(user_lat, output_field=FloatField())) *
    #                     Cos(
    #                         Radians(models.F("lng"), output_field=FloatField()) -
    #                         Radians(user_lng, output_field=FloatField()),
    #                         output_field=FloatField()
    #                     ) +
    #                     Sin(Radians(models.F("lat"), output_field=FloatField())) *
    #                     Sin(Radians(user_lat, output_field=FloatField()))
    #                 ),
    #         )
    #         .order_by("distance")
    #         .first()
    #     )

    #     if nearest:
    #         return JsonResponse({
    #             "status": "success",
    #             "location": nearest.name,
    #             "geohash": nearest.geohash,
    #             "nearest_city": nearest.city.name if nearest.city else None,
    #             "distance_meters": nearest.distance
    #         })

    #     return JsonResponse({"status": "no_locations_found"})

class SearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        results = Category.objects.filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))[:10]
        data = [{'name': cat.name, 'slug': cat.slug} for cat in results]
        return JsonResponse({'results': data})