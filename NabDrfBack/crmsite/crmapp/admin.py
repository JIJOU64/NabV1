from django.contrib import admin
from .models import UserProfile, ClientProgress, TrainingOutline, TrainingStatus

# Register your models here.
#admin.site.register(UserProfile)
admin.site.register(ClientProgress)
admin.site.register(TrainingOutline)
admin.site.register(TrainingStatus)

