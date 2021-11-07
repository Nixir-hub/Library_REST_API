from rest_framework import generics

from booksloans.models import Library, LoanBook
from booksloans.serializers import LibrarySerializer, LoanBookSerializer


class LibraryListView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class LibraryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class LoanBookListView(generics.ListCreateAPIView):
    queryset = LoanBook.objects.all()
    serializer_class = LoanBookSerializer


class LoanBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanBook.objects.all()
    serializer_class = LoanBookSerializer
