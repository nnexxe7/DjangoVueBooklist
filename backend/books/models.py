from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to="", default="")

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Book)
def delete_book_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
