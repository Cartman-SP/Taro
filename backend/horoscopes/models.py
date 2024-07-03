from django.db import models

class Horoscope(models.Model):
    sign = models.CharField(max_length=20, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.sign
