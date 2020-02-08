from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

import messaging.views as mssg_views

router = routers.DefaultRouter()
# router.register(r'add-client', sud_views.AddClient)

app_name = 'messaging'
urlpatterns = [
    # url(r'^', include(router.urls)),
    
]