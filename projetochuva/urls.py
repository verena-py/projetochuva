from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('piaui.urls')),
    path('', include('odm2.urls')),
]




