from django.db import models


class TemporaryAlienAccount(models.Model):
    username = models.CharField(max_length=64, blank=False, null=False)
    real_name = models.CharField(max_length=255, blank=False, null=False)
    #    password = models.P
    valid_until = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f'{self.username} [ALIEN]'