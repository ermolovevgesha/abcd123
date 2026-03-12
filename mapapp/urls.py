from django.urls import path

from mapapp.views import PointsView


urlpatterns = [
    path('points/', PointsView.as_view()),
]

