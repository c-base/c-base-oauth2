from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    real_name = models.CharField(max_length=255, blank=True, null=True)
    is_temporary_alien = models.BooleanField(default=False)
    valid_until = models.DateTimeField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)   # numerical UNIX user ID as determined by LDAP

    def __str__(self):
        if self.is_temporary_alien:
            return f'{self.username} [ALIEN]'
        else:
            return self.username
