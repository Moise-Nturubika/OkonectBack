from . import views
from django.urls import path

urlpatterns = [
    path('all/save', views.saveMedia),
    path('show/all', views.fecthAllMedia),
    path('show/key/<int:id>', views.fecthMediaById),
    path('show/category/<str:category>', views.fecthMediaByCategory),
    path('update', views.updateMedia),
    path('delete', views.deleteMedia),
]
