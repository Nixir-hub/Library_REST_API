from random import choice
from faker import Faker
from bookslist.models import Book, Author


faker = Faker("pl_PL")


def random_person():
    """Return a random Author object from db."""
    people = Author.objects.all()
    return choice(people)


def fake_book_data():
    """Generate a dict of book data

    The format is compatible with serializers (`Author` relations
    represented by names).
    """
    book_data = {
        "title": f"{faker.job()} {faker.first_name()}",
        "description": faker.sentence(),
        "author": random_person().name,
        "year": int(faker.year())
    }
    return book_data


def find_person_by_name(name):
    """Return the first `Book` object that matches `name`."""
    return Author.objects.filter(name=name).first()


def create_fake_book():
    """Generate new fake book and save to database."""
    book_data = fake_book_data()
    book_data['author'] = find_person_by_name(book_data['author'])
    new_book = Book.objects.create(**book_data)
    return new_book


