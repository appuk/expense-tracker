from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_bonus, name='add_bonus'),
]