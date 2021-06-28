from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('category/', include('main.urls')),
    path('card/', include('django.contrib.auth.urls')),
    path('categorycard/', include('django.contrib.auth.urls')),
    path('recomendation/', include('main.urls')),
    path('createrecom/', include('main.urls')),
    path('tableproduct/', include('main.urls')),
    path('createrecipe/', include('main.urls')),
    path('dictionary/', include('main.urls')),
    path('dashboard/', include('main.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.BASE_DIR, settings.MEDIA_ROOT)
