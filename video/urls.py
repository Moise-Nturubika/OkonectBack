from . import views
from django.urls import path

urlpatterns = [
    path('all/save', views.saveMedia),
    path('show/all', views.fetchAllMedia),
    path('show/key/<int:id>', views.fetchMediaById),
    path('show/top', views.fetchTopMedia),
    path('show/caroussel', views.fetchCarousselMedia),
    path('show/recent', views.fetchRecentMedia),
    path('show/category/<str:category>', views.fetchMediaByCategory),
    path('category/search', views.fetchSearchedMediaByCategory),
    path('show/client/<str:pk>', views.fetchMediaClient),
    
    path('update', views.updateMedia),
    path('delete', views.deleteMedia),
    
    path('category/show/all', views.fetchAllCategory),
]
