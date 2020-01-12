from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile():
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(blank=True, max_length=30)
    time_token_created = models.CharField(blank=True, max_length=30)
    private_key = models.CharField(max_length=50)
    public_key = models.CharField(max_length=50)

    def __str__(self):
        return(self.user.username)