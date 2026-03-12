import json

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from django.views.generic import TemplateView

from mapapp.models import ClickLocation


class PointsView(View):
    def get(self, request):
        locations = ClickLocation.objects.all()
        return render(request, 'mapapp/point_list.html', {'locations': locations})
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            lng = float(data.get('lng'))
            lat = float(data.get('lat'))
        except (json.JSONDecodeError, TypeError, ValueError, KeyError):
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        point = Point(lng, lat)
        ClickLocation.objects.create(point=point)
        
        return JsonResponse({'status': 'ok'})


class MapView(TemplateView):
    template_name = 'mapapp/map.html'


