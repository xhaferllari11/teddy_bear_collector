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
]