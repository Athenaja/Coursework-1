from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('accounts/', include('django.contrib.auth.urls')),
]

