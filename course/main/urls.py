from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('category/', views.category),
    path('card/', views.card),
    path('recomendation/', views.recom),
    path('createrecom/', views.createrecom),
    path('tableproduct/', views.tablepr),
    path('createrecipe/', views.createrecipe),
    path('dictionary/', views.dictionary),
    path('equipmentTips/', views.equipmentTips),
    path('dashboard/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('dashboard/data/', views.pivot_data, name='pivot_data'),
]

