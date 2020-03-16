import profiles.models as pro_models
from rest_framework import permissions


class TokenAuthenticate(permissions.BasePermission):
	# Not Used Anywhere right now
    def has_permission(self, request, view):
        profile_id = request.data['id']
        profile_token = request.data['token']
        if(pro_models.Profile.objects.filter(id = profile_id, token = profile_token)):
            return(True)
        return(False)