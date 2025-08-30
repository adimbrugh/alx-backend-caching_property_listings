from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property



# Apply caching for 15 minutes (60 * 15 seconds)
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all(
        "id", "title", "description", "price", "location", "created_at"
    )
    return JsonResponse({"data": list(properties)})  # Return properties as JSON response
    #return render(request, "properties/property_list.html", {"properties": properties}) # Render the property list template with the properties context
