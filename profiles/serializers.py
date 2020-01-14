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
        user_profile = pro_models.Profile.objects.create(user = new_user, 
            token = pro_utils.random_string_generator(), time_token_created = pro_utils.current_milli_time(),
            private_key = pro_utils.random_string_generator(), public_key = pro_utils.random_string_generator())
        return(new_user)

    # def update(self, instance, validated_data):

    #     cp = instance.clientprofile
    #     clientprofile_data = validated_data.pop('clientprofile')

    #     for field_name, value in validated_data.items():
    #         setattr(instance, field_name, value)
    #     instance.save()
        
    #     for field_name, value in clientprofile_data.items():
    #         setattr(cp, field_name, value)
    #     cp.save()

    #     return(instance)

# class BaseProfileSerializer(serializers.ModelSerializer):
#     profile_user_details = BaseUserSerializer()
#     class Meta:
#         model = pro_models.Profile
#         fields = ('id', 'token', 'time_token_created', 'private_key', 'public_key', 'profile_user_details')

#     def create(self, validated_data):
#         print(validated_data)
#         profile_data = validated_data.pop('profile_user_details')
#         print(validated_data)
#         # client = client_models.Client.objects.create(**validated_data)
#         # cp = client.clientprofile

#         # for field_name, value in clientprofile_data.items():
#         #     setattr(cp, field_name, value)
#         # cp.save()

#         # return(client)

#         return({})

#     # def update(self, instance, validated_data):

#     #     cp = instance.clientprofile
#     #     clientprofile_data = validated_data.pop('clientprofile')

#     #     for field_name, value in validated_data.items():
#     #         setattr(instance, field_name, value)
#     #     instance.save()
        
#     #     for field_name, value in clientprofile_data.items():
#     #         setattr(cp, field_name, value)
#     #     cp.save()

#     #     return(instance)