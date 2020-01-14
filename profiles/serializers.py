import time
import profiles.models as pro_models
import profiles.utils as pro_utils
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model();

# fields = ('id', 'token', 'time_token_created', 'private_key', 'public_key', 'profile_user_details')
# fields = ('username', 'email', 'password', 'first name', 'last name')

class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = pro_models.Profile
        fields = ('token', 'time_token_created', 'private_key', 'public_key')

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        # user_profile = pro_models.Profile.objects.create(user = user, token = ,
        #             time_token_created = pro_utils.current_milli_time, private_key = , public_key =)

        return(new_user)
        return(user_profile.token)

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