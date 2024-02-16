from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name= 'index'),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
]
