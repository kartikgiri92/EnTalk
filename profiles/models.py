from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile():
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    identification_num = models.IntegerField()

    token = models.CharField(blank=True, max_length=30)

    time_token_created = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return(self.user.email)