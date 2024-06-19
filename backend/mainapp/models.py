from django.db import models
from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=128)
    usertag = models.CharField(max_length=128)
    sub_date = models.DateField()

class Order(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    tariff = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=255,)
    is_paid = models.BooleanField(default=False)