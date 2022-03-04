from . import views
from django.urls import path

urlpatterns = [
    path('save', views.saveClient),
    path('show/key/<int:pk>', views.fetchClientById),
    path('show/phone/<str:phone>', views.fetchClientByPhone),
]
