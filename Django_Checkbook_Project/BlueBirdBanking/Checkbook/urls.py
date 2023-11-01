from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='index'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('create/', views.create_account,name='create'),
    path('transaction/', views.transaction, name='transaction'),
]