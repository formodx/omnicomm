from django.db import models

from ..common.models import CreatedUpdatedDeleted


class Tutorial(CreatedUpdatedDeleted):
    text = models.TextField(verbose_name='Text')
    video = models.FileField(verbose_name='Video')

    def __str__(self):
        return f'Tutorial: {self.id}'