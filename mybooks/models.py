from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    languages = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title