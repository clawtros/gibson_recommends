from django.db import models
from tagging.models import Tag
from tagging.managers import ModelTagManager, ModelTaggedItemManager
from tagging.fields import TagField
from django.db.models.signals import pre_save
import tagging
import geocode

class Place(models.Model):
    name = models.CharField(null=True, blank=True,max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=2000,null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    
    time_updated = models.DateTimeField(null=True, blank=True)
    objects = models.Manager()
    tag_manager = ModelTagManager()
    tagged_item_manager = ModelTaggedItemManager()
    tags = TagField()
    
    def _get_tags(self):
        return Tag.objects.get_for_object(self)
    def _set_tags(self, tag_list):
        Tag.objects.update_tags(self, tag_list)

    tags = property(_get_tags, _set_tags)

    def __unicode__(self):
        return "%s %s (%s,%s)" % (self.name, self.address, self.lat, self.lng)

def update_location(sender, instance, **kwargs):
    location = geocode.geocode(instance.address)    
    instance.lng = location['longitude']
    instance.lat = location['latitude']

pre_save.connect(update_location, sender=Place)
