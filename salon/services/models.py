from django.db import models


class Servicec(models.Model):
    title = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
