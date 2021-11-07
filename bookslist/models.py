from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " " + self.surname


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, related_name="books_written", on_delete=models.CASCADE)
    year = models.SmallIntegerField()
