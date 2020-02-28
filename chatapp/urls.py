from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.site.site_header = 'ChatApp Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profiles/', include('profiles.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('', TemplateView.as_view(template_name="profiles/login_sign_up.html")),
    path('dashboard/', TemplateView.as_view(template_name="messaging/dashboard.html")),

]
