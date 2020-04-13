import profiles.models as pro_models
import profiles.utils as pro_utils
import profiles.serializers as pro_serializers

import messaging.models as mssg_models
import messaging.utils as mssg_utils
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

class GetChat(ListAPIView):
    def list(self, request, *args, **kwargs):
        token_auth, profile = pro_utils.TokenAuthenticate(request)
        if(not(token_auth)):
            return(Response({'message':'User Logged Out', 'status':False, 'token': False}))

        try:
            friend_profile = pro_models.Profile.objects.get(id = request.headers['Friend'])
        except:
            # except pro_models.Profile.DoesNotExist:
            return(Response({'message':'Friend Not Exist', 'status':False, 'token' : True}))

        user, friend = profile.user, friend_profile.user
        all_mssgs = mssg_models.Message.objects.filter( Q(receiver = friend) & Q(sender = user) | Q(receiver = user) & Q(sender = friend))\
                    .order_by('date_time')

        data = {'friend_data' : {'username':friend.username}, 'messages' : []}
        for mssg in all_mssgs:
            if(mssg.sender == user):
                dcy_mssg = mssg_utils.decrypt_message(friend_profile, mssg.mssg)
                data['messages'].append(['0', dcy_mssg])
            else:
                dcy_mssg = mssg_utils.decrypt_message(profile, mssg.mssg)
                data['messages'].append(['1', dcy_mssg])
        return(Response({'message':'All Chats in data field', 'status':True, 'token':True, 'data' : data}))

class MessageView(CreateAPIView, RetrieveAPIView):
    serializer_class = mssg_serializers.BaseMessagingSerializer

    def create(self, request, *args, **kwargs):
        token_auth, profile = pro_utils.TokenAuthenticate(request)
        if(not(token_auth)):
            return(Response({'message':'User Logged Out', 'status':False, 'token': False}))
        try:
            friend_profile = pro_models.Profile.objects.get(id = request.headers['Friend'])
        except:
            # except pro_models.Profile.DoesNotExist:
            return(Response({'message':'Friend Not Exist', 'status':False, 'token' : True}))

        user, friend = profile.user, friend_profile.user
        enc_mssg = mssg_utils.encrypt_message(friend_profile, request.data['message'])
        mssg_models.Message.objects.create(sender = user, receiver = friend, mssg = enc_mssg)

        return(Response({'message':'Message Created Successfully', 'status':True, 'token':True}))