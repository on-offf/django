from django.db import models

class Image(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField()

    def __str__(self):
        return self.title
