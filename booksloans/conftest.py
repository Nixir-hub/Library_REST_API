import os
import sys

import pytest
from faker import Faker
from rest_framework.test import APIClient

from bookslist.models import Author
from booksloans.models import Library
from bookslist.utils import create_fake_book
from booksloans.utils import create_fake_library

sys.path.append(os.path.dirname(__file__))
faker = Faker("pl_PL")


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(5):
        Author.objects.create(name=faker.name(), surname=faker.name())
    for _ in range(10):
        create_fake_book()
    for _ in range(3):
        create_fake_library()


@pytest.fixture
def library():
    lib = Library.objects.create(name=faker.name(), city=faker.city())
    return lib
