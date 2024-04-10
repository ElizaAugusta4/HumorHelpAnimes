from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    humor = models.CharField(max_length=100)

    def __str__(self):
        return self.title
