from django.urls import path

from main_app.models import Accessories
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('duckies/', views.duckies_index, name='index'),
    path('duckies/<int:duck_id>', views.duckies_detail, name='detail'),
    path('duckies/create/', views.DuckCreate.as_view(), name='ducks_create'),
    path('duckies/<int:pk>/update/', views.DuckUpdate.as_view(), name='ducks_update'),
    path('duckies/<int:pk>/delete/', views.DuckDelete.as_view(), name='ducks_delete'),
    path('duckies/<int:duck_id>/add_location/', views.add_location, name='add_location'),
    path('accessories/', views.AccessorieList.as_view(), name = 'accessories_index'),
    path('accessories/<int:pk>/', views.AccessorieDetail.as_view(), name = 'accessories_detail'),
    path('accessories/create', views.AccessorieCreate.as_view(), name = 'accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessorieUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessorieDelete.as_view(), name ='accessories_delete'),
    path('duckies/<int:duck_id>/assoc_access/<int:accessorie_id>/', views.assoc_access, name='assoc_access'),

]