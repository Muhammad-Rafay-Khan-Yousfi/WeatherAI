from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("location/", views.location, name="location"),
    path("current-weather/", views.current_weather, name="current_weather"),
    path("forecast/", views.forecast, name="forecast"),
    path("alerts/", views.alerts, name="alerts"),
    path("farming/", views.farming, name="farming"),
    path("farming-api/", views.farming_api, name="farming_api"),
    path("weather/", views.weather, name="weather"),
    path("alerts-api/", views.alerts_api, name="alerts_api"),
]