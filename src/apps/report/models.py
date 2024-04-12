from django.contrib.auth import get_user_model
from django.db import models

from ..common.models import CreatedUpdatedDeleted


User = get_user_model()


class Status(CreatedUpdatedDeleted):
    class Meta:
        verbose_name_plural = 'Statuses'

    title = models.CharField('Title', max_length=100)

    def __str__(self):
        return self.title


class Report(CreatedUpdatedDeleted):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text')
    deadline = models.DateTimeField('Deadline')

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_sender')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='report_status')
    files = models.ManyToManyField('common.File')
    recipients = models.ManyToManyField(User)

    def __str__(self):
        return self.title