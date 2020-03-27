from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

import profiles.views as pro_views

router = routers.DefaultRouter()
# router.register(r'add-client', sud_views.AddClient)

app_name = 'profiles'
urlpatterns = [
    # url(r'^', include(router.urls)),

    path('login/', pro_views.UserLogin.as_view()),
    path('logout/', pro_views.UserLogout.as_view()),
    path('create/', pro_views.CreateUser.as_view()),
    path('rtd/', pro_views.RetrieveUserDetail.as_view()),
    path('searchfriend/', pro_views.SearchFriend.as_view()),
    
]