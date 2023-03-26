from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image


class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/images/')
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
