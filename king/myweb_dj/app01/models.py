from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    user_type = models.IntegerField(default=1)
