from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

admin.site.site_header = 'ChatApp Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profiles/', include('profiles.urls')),
]
