from .models import Location
def business_data(request):
    locations = Location.objects.all()
    return {
        'locations': locations
    }