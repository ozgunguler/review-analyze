import uuid

from django.contrib.auth.models import AbstractUser
from djongo import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    id = models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, editable=True)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def data(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token)
        }

    class Meta:
        db_table = "user"
