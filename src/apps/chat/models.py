from django.contrib.auth import get_user_model
from django.db import models

from ..common.models import CreatedUpdatedDeleted


User = get_user_model()


class Chat(CreatedUpdatedDeleted):
    title = models.CharField('Title', max_length=100)
    participants = models.ManyToManyField(User)
    avatar = models.ImageField('Avatar', blank=True, null=True)

    def __str__(self):
        return self.title