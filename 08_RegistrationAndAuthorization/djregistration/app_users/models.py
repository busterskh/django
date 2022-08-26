from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='Телефон')
    city = models.CharField(max_length=50, verbose_name='Город')
    is_verification = models.BooleanField(default=False)
    news_count = models.IntegerField(default=0)
    id = models.IntegerField(primary_key=True)
