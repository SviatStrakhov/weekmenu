from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    class Meta(object):
        verbose_name = 'User Profile'

    mobile_phone = models.CharField(
        max_length=12,
        blank=True,
        verbose_name='Mobile Phone',
        default=''
    )

    def __str__(self):
        return f'{self.user.username}'
