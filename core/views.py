from django.shortcuts import render
from django.views import View
import pygeohash as pgh
import requests
from business.utils import get_geohash_neighbors
# Create your views here.

GOOGLE_KEY = "AIzaSyC3mNT02ooGBr5NcWGUMb-cyNpVMJWG-Uc"

class HomeView(View):
    template_name = 'core/index.html'
    def get(self, request):
        return render(request, self.template_name)
    
def get_localities(lat, lng):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{lat},{lng}",
        "key": GOOGLE_KEY
    }
    r = requests.get(url, params=params).json()

    localities = []

    for result in r.get("results", []):
        types = result["types"]
        if "sublocality" in types or "locality" in types:
            localities.append({
                "name": result["formatted_address"],
                "lat": lat,
                "lng": lng
            })
    
    return localities
    
class LocationView(View):
    template_name = 'location.html'
    
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)