from models import Place
from django.db.models import Avg, Max, Min

def map_vars(request):
    places = Place.objects.all()
    cloud = Place.tag_manager.cloud()
    if request.GET.get('tag'):
        places = Place.tagged_item_manager.with_any([request.GET.get('tag'),])
    avgs = places.aggregate(Avg('lng'),Avg('lat'),Max('lng'),Max('lat'),Min('lng'), Min('lat'))
    return {'places': places,
            'cloud' : cloud,
            'avg_lng' : avgs['lng__avg'],
            'avg_lat' : avgs['lat__avg'],
            'min_lng' : avgs['lng__min'],
            'min_lat' : avgs['lat__min'],
            'max_lng' : avgs['lng__max'],
            'max_lat' : avgs['lat__max'],
            }
