

from django.urls import path
from .views import property_list, cache_metrics



# URL patterns for the properties app
urlpatterns = [
    path("", property_list, name="property_list"),
    path("metrics/", cache_metrics, name="cache_metrics"),
]
