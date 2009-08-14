# Create your views here.
from models import Place
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import PlaceForm



def index(request):
    return render_to_response('base.html',{},RequestContext(request))



def edit_place(request, place_id, **kwargs):
    place = Place.objects.get(id=place_id)

    if request.POST:
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save(force_update=True)
    else:
        form = PlaceForm(instance=place)

    context = {'form':form}
    return render_to_response('place/form.html',context,RequestContext(request))

def add_place(request, **kwargs):
    form = None

    if request.POST:
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PlaceForm()

    context = {'form':form}
    return render_to_response('place/form.html',context,RequestContext(request))
