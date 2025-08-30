

from django.core.cache import cache
from .models import Property



def get_all_properties():
    """
    Returns all properties, cached in Redis for 1 hour.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(
            Property.objects.all().values(
                "id", "title", "description", "price", "location", "created_at"
            )
        )
        cache.set('all_properties', properties, 3600)  # cache for 1 hour
    return properties
