from django.contrib.auth import get_user_model
from django.db import models

from ..common.models import CreatedUpdatedDeleted


User = get_user_model()


class Message(CreatedUpdatedDeleted):
    text = models.TextField('Text')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey('chat.Chat', on_delete=models.CASCADE)


    def __str__(self):
        return f'Message from {self.user} in {self.chat} chat'