from django.db import models


class Master(models.Model):
    LOCATION = (
        ('1', 'Шишкина'),
        ('2', 'Заречная')
    )
    photo = models.ImageField(upload_to='masters/images/')
    name = models.CharField(max_length=200)
    specialization = models.TextField()
    link = models.URLField()
    location = models.CharField(max_length=1, choices=LOCATION)

    def __str__(self):
        return self.name
