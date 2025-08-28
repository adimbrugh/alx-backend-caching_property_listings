

from django.urls import path
from .views import property_list



# URL patterns for the properties app
urlpatterns = [
    path("", property_list, name="property_list"),
]
