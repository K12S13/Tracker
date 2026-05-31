from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habits_list'),
    path('create/', views.habit_create, name='habits_create'),
    path('<int:habit_id>/done/', views.habit_done, name='habits_done'),
    path('<int:habit_id>/delete/', views.habit_delete, name='habits_delete'),
]