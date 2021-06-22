from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('category/', views.category),
    path('card/', views.card),
    path('recomendation/', views.recom),
    path('recomendation/createrecom/', views.createrecom)
]

