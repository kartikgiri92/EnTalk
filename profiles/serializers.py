import time
import profiles.models as pro_models
import profiles.utils as pro_utils
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model();

class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = pro_models.Profile
        fields = ('token', 'time_token_created', 'private_key', 'public_key')

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(self.context.data['password'])
        new_user.save()

        private_key, public_key, public_key_2 = pro_utils.generate_secret_keys()
        while((len(private_key) > 30) or (len(public_key) > 30) or (len(public_key_2) > 30)):
            private_key, public_key, public_key_2 = pro_utils.generate_secret_keys()

        user_profile = pro_models.Profile.objects.create(user = new_user, 
            token = pro_utils.token_generator(), time_token_created = pro_utils.current_milli_time(),
            private_key = private_key, public_key = public_key, public_key_2 = public_key_2)
        return(new_user)

    def update(self, instance, validated_data):
        for field_name, value in validated_data.items():
            setattr(instance, field_name, value)
        instance.set_password(self.context.data['new_password'])
        instance.save()
        return(instance)