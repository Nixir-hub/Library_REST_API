from random import sample
import pytz
from faker import Faker
from booksloans.models import LoanBook, Library
from books.settings import TIME_ZONE
from bookslist.models import Book


faker = Faker("en_US")
TZ = pytz.timezone(TIME_ZONE)


def random_books():
    """Return 3 random Books from db."""
    books = list(Book.objects.all())
    return sample(books, 3)


def add_loans(library):
    """Add 3 loans for library."""
    books = random_books()
    for book in books:
        LoanBook.objects.create(library=library, book=book, date=faker.date_time(tzinfo=TZ))


def fake_library_data():
    """Generate fake data for library."""
    lib_data = {
        "name": faker.name(),
        "city": faker.city(),
    }
    return lib_data


def create_fake_library():
    """Create fake library with some loans."""
    library = Library.objects.create(**fake_library_data())
    add_loans(library)
