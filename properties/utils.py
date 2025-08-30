

from django_redis import get_redis_connection
from django.core.cache import cache
from .models import Property
import logging



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



logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieves Redis cache hit/miss metrics and calculates hit ratio.
    Returns a dictionary with the metrics.
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info("stats")

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0.0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 2),
    }

    logger.info(f"Redis Cache Metrics: {metrics}")
    return metrics
