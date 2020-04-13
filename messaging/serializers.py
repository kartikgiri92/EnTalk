import time
import messaging.models as mssg_models
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model();

class BaseMessagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = mssg_models.Message
        fields = ('mssg')