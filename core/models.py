from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=80)
    director = models.CharField(max_length=80)

    def __str__(self):
        return self.name