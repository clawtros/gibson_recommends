from django.conf.urls.defaults import *
from goodplaces import views as place_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^place/add/$',place_views.add_place),
                       (r'^place/edit/(?P<place_id>\d+)/$',place_views.edit_place),
                       (r'^admin/', include(admin.site.urls)),
                       (r'.*',place_views.index),
)
