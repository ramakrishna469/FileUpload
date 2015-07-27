from django.db import models

# Create your models here.
class FileUpload(models.Model):
    File = models.FileField(upload_to='fileuploader')

    def __str__(self):
        return self.File.name
