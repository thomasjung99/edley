from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),       # ruft ..\telefonbuch\views.py auf
    path('eintraege', views.eintraege),
]