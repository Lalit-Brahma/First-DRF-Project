from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='titan-home'),
    path('shopping/', views.shopping, name='titan-shopping'),
    path('weapons/', views.weapons, name='titan-weapons'),
    path('clothes/', views.clothes, name='titan-clothes'),
    path('food/', views.food, name='titan-food'),
    path('transaction/', views.transaction, name='titan-transaction'),
    
]