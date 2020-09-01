from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', index, name='index')
]
