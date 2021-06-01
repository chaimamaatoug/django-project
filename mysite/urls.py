from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
        path('gest/', include('gestionprojet.urls')),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
