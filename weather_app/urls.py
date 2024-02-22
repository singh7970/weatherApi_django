from django.urls import path
# from weather_app import views
from . import views
urlpatterns = [
    path('',views.index)
]
