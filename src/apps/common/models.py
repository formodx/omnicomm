from django.db import models


class CreatedUpdatedDeleted(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    deleted_at = models.DateTimeField('Deleted at', blank=True, null=True)


class File(CreatedUpdatedDeleted):
    def upload_to(instance, filename):
        return filename

    file = models.FileField('File', upload_to=upload_to, max_length=100)

    def __str__(self):
        return str(self.file)