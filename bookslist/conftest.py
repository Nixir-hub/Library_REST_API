import os
import sys
import pytest
from rest_framework.test import APIClient

from booksloans.utils import create_fake_library
from .utils import faker, create_fake_book
from bookslist.models import Author, Book

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(5):
        Author.objects.create(name=faker.name(), surname=faker.name())
    for _ in range(3):
        create_fake_book()
    for _ in range(3):
        create_fake_library()

@pytest.fixture
def author():
    author = Author.objects.create(name=faker.name(), surname=faker.surname())
    return author


@pytest.fixture
def book(author):
    book = Book.objects.create(title=faker.title(), description=faker.description(), author=author.id, year=faker.year())
    return book

