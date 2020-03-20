import profiles.models as pro_models
import profiles.utils as pro_utils
import profiles.serializers as pro_serializers

import messaging.models as mssg_models
import messaging.serializers as mssg_serializers

import time
from django.db.models import Q
from django.db import connection, reset_queries
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (ListAPIView, 
    CreateAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView,
    RetrieveUpdateAPIView, GenericAPIView
)

User = get_user_model();

# To Check Number of Query Execution #
# print(len(connection.queries))
# reset_queries()

class GetAllChats(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(profile__id = request.headers['Id'])
        except User.DoesNotExist:
            return(Response({'message':'Wrong User', 'status':False}))
        
        data, conv_dic = [], {}
        all_mssgs = mssg_models.Message.objects.filter( Q(sender = user) | Q(receiver = user) ).select_related('sender', 'receiver')
        for mssg in all_mssgs:
            temp = None
            if(mssg.sender == user):    temp = mssg.receiver
            else:   temp = mssg.sender

            if(temp in conv_dic):   conv_dic[temp] += 1
            else:   conv_dic[temp] = 1

        temp = list(conv_dic.keys())
        for user_obj in temp:
            data.append({'profile_id':user_obj.profile.id, 
                            'username':user_obj.username,
                            'total_messages':conv_dic[user_obj]})

        return(Response({'message':'All Chats in data field', 'status':True, 'data' : data}))

# class UserLogin(GenericAPIView):

#     def post(self, request):
#         user = User.objects.filter(username = request.data['username'])
#         if(not(user) or not(user[0].check_password(request.data['password']))):
#             return(Response({'message':'UserName or Password is Wrong', 'status':False}))
#         user = user[0]
#         if(pro_models.Profile.objects.filter(user = user).exists()):
#             user.profile.token = pro_utils.token_generator()
#             user.profile.time_token_created = pro_utils.current_milli_time()
#             user.profile.save()
#         else:
#             user_profile = pro_models.Profile.objects.create(user = user, 
#                 token = pro_utils.token_generator(), time_token_created = pro_utils.current_milli_time(),
#                 private_key = pro_utils.random_string_generator(), public_key = pro_utils.random_string_generator())

#         user_data = pro_serializers.BaseUserSerializer(user)
#         return Response({'message':'User Successfully Logged In', 'status':True,
#             'user' : user_data.data, 'token' : user.profile.token, 'id': user.profile.id})

# class UserLogout(GenericAPIView):

#     def get(self, request):
#         token_auth, profile = pro_utils.TokenAuthenticate(request)
#         if(not(token_auth)):
#             return(Response({'message':'User Logged Out', 'status':False, 'token': False}))

#         profile.token = profile.time_token_created = ''
#         profile.save()
#         return(Response({'message':'User Logged Out', 'status':True, 'token': True}))

# class CreateUser(CreateAPIView, UpdateAPIView):
#     serializer_class = pro_serializers.BaseUserSerializer
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context = request)

#         if(not(serializer.is_valid())):
#             errors = list(serializer.errors.keys())
#             return Response({'message':'User Not Created', 'status':False, 'errors' : errors})
#         self.perform_create(serializer)
#         new_user = User.objects.get(username = serializer.data['username'])
#         return Response({'message':'User Created Successfully', 'status':True,
#             'user' : serializer.data, 'token' : new_user.profile.token, 'id': new_user.profile.id})

#     def update(self, request, *args, **kwargs):
#         token_auth, profile = pro_utils.TokenAuthenticate(request)
#         if(not(token_auth)):
#             return(Response({'message':'User Logged Out', 'status':False, 'token': False}))

#         instance = profile.user
#         serializer = self.serializer_class(instance, data=request.data, context = request, partial = True)
#         if(not(serializer.is_valid())):
#             errors = list(serializer.errors.keys())
#             return Response({'message':'User Not Updated', 'status':False, 'errors' : errors, 'token' : True})
#         if(not(profile.user.check_password(request.data['current_password']))):
#             return Response({'message':'User Not Updated', 'status':False, 'errors' : [' Current Password is Wrong'], 'token' : True})

#         self.perform_update(serializer)
#         return Response({'message':'User Updated Successfully', 'status':True,
#             'user' : serializer.data, 'token' : True})