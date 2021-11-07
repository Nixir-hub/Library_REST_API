from rest_framework import serializers
from bookslist.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ("id", "title", "year", "description", "author")


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "name", "surname")
