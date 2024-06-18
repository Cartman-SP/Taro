from django.db import models
from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=128)
    usertag = models.CharField(max_length=128)
    sub_date = models.DateField()

