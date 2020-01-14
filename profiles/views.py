import profiles.models as pro_models
import profiles.utils as pro_utils
import profiles.serializers as pro_serializers

import time
from rest_framework.parsers import FileUploadParser
from django.db import connection, reset_queries
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ( ListAPIView, 
    CreateAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView,
    RetrieveUpdateAPIView
)

User = get_user_model();

# To Check Number of Query Execution #
# print(len(connection.queries))
# reset_queries()

class CreateUser(CreateAPIView):
    serializer_class = pro_serializers.BaseUserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if(not(serializer.is_valid())):
            errors = list(serializer.errors.keys())
            return Response({'message':'User Not Created', 'status':False, 'errors' : errors})
        self.perform_create(serializer)
        return Response({'message':'User Created Succesfully', 'status':True, 'token' : ''})