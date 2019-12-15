from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teddys/', views.teddys_index, name='index'),
    path('teddys/<int:teddy_id>/', views.teddys_detail, name='detail'),
]