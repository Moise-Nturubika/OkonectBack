from django.urls import path
from . import views

urlpatterns = [
    path('save', views.saveChat),
    path('canal/show/all', views.fetchAllChannels),
    path('canal/show/<int:canal>', views.fetchCanalChat),
]
