from django.contrib import admin
import messaging.models as mssg_models

# Register your models here.
admin.site.register(mssg_models.Message)