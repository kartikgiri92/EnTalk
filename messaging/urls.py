from django.conf.urls import include, url
from django.urls import path

import messaging.views as mssg_views

app_name = 'messaging'
urlpatterns = [

    path('gac/', mssg_views.GetAllChats.as_view()),
    
]