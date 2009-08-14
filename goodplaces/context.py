from models import Place
from django.db.models import Avg

def map_vars(request):
    places = Place.objects.all()
    avgs = places.aggregate(Avg('lng'),Avg('lat'))
    cloud = Place.tag_manager.cloud()
    if request.GET.get('tag'):
        places = Place.tagged_item_manager.with_any([request.GET.get('tag'),])
    return {'places': places,
            'cloud' : cloud,
            'avg_lng' : avgs['lng__avg'],
            'avg_lat' : avgs['lat__avg']}
