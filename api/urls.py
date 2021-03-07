from django.urls import path
from .views.compradores import CompradoresApi,SpecificCompradoresApi,GeoCodeCompradoresApi


urlpatterns = [
    path('compradores',CompradoresApi.as_view()),
    path('compradores/<int:id>',SpecificCompradoresApi.as_view()),
    path('compradores/geocode',GeoCodeCompradoresApi.as_view()),
]