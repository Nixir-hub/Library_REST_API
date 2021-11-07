from django.db import models

from bookslist.models import Book


class Library(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, through="LoanBook")


class LoanBook(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField()

