from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/images/')
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title