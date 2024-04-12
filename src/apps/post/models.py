from django.contrib.auth import get_user_model
from django.db import models

from ..common.models import CreatedUpdatedDeleted


User = get_user_model()

class Post(CreatedUpdatedDeleted):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text')
    image = models.ImageField('Image')

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title