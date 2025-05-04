from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newapp.urls')),  # inclui as URLs do seu app
]
