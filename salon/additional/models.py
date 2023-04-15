from django.db import models


class Photos(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='additional/images/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

