from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teddys/', views.teddys_index, name='index'),
    path('teddys/<int:teddy_id>/', views.teddys_detail, name='detail'),
    path('teddys/create/', views.TeddyCreate.as_view(), name='teddy_create'),
    path('teddys/<int:pk>/update/', views.TeddyUpdate.as_view(), name='teddy_update'),
    path('teddys/<int:pk>/delete/', views.TeddyDelete.as_view(), name='teddy_delete'),
    path('teddys/<int:teddy_id>/add_cleaning', views.add_cleaning, name='add_cleaning'),
    path('teddys/<int:teddy_id>/assoc_cloth/<int:cloth_id>/', views.assoc_cloth, name='assoc_cloth'),
    path('clothes/', views.ClothesList.as_view() , name='clothes_index'),
    path('clothes/<int:pk>/', views.ClothesDetail.as_view() , name='clothes_detail'),
    path('clothes/create/', views.ClothesCreate.as_view() , name='clothes_create'),
    path('clothes/<int:pk>/update', views.ClothesUpdate.as_view() , name='clothes_update'),
    path('clothes/<int:pk>/delete', views.ClothesDelete.as_view() , name='clothes_delete'),
]