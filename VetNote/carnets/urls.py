from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='carnets'),
    path('<int:carnet_id>', views.carnet, name='carnet'),
    path('search', views.search, name='search'),
]