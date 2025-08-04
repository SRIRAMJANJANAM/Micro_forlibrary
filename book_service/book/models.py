from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=120)
    year = models.DateField()

    def __str__(self):
        return self.name
