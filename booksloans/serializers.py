import pytz
from rest_framework import serializers
from booksloans.models import Library, LoanBook
from books.settings import TIME_ZONE
from bookslist.models import Book

TZ = pytz.timezone(TIME_ZONE)


class LibrarySerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='library-detail'
    )

    class Meta:
        model = Library
        fields = ['name', 'city', 'books']


class LoanBookSerializer(serializers.ModelSerializer):
    library = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Library.objects.all()
    )
    book = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Book.objects.all()
    )

    class Meta:
        model = LoanBook
        fields = ['library', 'book', 'date']
