from django.urls import path
from . import views

urlpatterns = {
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('duckies/', views.duckies_index, name='index'),
    path('duckies/<int:duck_id>', views.duckies_detail, name='detail'),
    path('duckies/create/', views.DuckCreate.as_view(), name='ducks_create'),
    path('duckies/<int:pk/update/', views.DuckUpdate.as_view(), name='ducks_update'),
    path('duckies/<int:pk/delete/', views.DuckDelete.as_view(), name='ducks_delete'),
}