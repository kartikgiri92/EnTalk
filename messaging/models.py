from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, related_name = "sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name = "receiver", on_delete=models.CASCADE)
    mssg = models.TextField(default='')
    date_time = models.DateTimeField(auto_now_add=True)
    # secret = models.BooleanField(default=False)

    def __str__(self):
        return(self.sender.username)