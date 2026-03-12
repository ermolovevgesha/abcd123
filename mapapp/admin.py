from django.contrib.gis import admin
from mapapp.models import ClickLocation


@admin.register(ClickLocation)
class ClickLocationAdmin(admin.GISModelAdmin):
    
    list_display = ('id', 'point', 'created_at')
    
    default_zoom = 12
    
    
