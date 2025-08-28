from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from .models import Property



# Apply caching for 15 minutes (60 * 15 seconds)
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
    return render(request, "properties/property_list.html", {"properties": properties}) # Render the property list template with the properties context
