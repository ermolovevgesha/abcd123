from django.urls import path

from mapapp.views import PointsView, MapView


urlpatterns = [
    path('points/', PointsView.as_view()),
    path('map/', MapView.as_view()),
]

