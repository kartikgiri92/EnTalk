import profiles.models as pro_models
import profiles.serializers as pro_serializers

import time
from rest_framework.parsers import FileUploadParser
from django.db import connection, reset_queries
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
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


class All_Users(ListAPIView):
    queryset = User.objects.all()
    serializer_class = pro_serializers.UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response({'data':serializer.data,'status':True})