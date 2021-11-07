import pytest
from .utils import fake_book_data
from bookslist.models import Book


@pytest.mark.django_db
def test_post_book(client, set_up):
    books_before = Book.objects.count()
    new_book = fake_book_data()
    response = client.post("/books/", new_book, format='json')
    assert response.status_code == 201
    assert Book.objects.count() == books_before + 1
    for key, value in new_book.items():
        assert key in response.data
        if isinstance(value, list):
            # Compare contents regardless of their order
            assert len(response.data[key]) == len(value)
        else:
            assert response.data[key] == value


@pytest.mark.django_db
def test_get_book_list(client, set_up):
    response = client.get("/books/", {}, format='json')

    assert response.status_code == 200
    assert Book.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_book_detail(client, set_up):
    book = Book.objects.first()
    response = client.get(f"/books/{book.id}/", {}, format='json')

    assert response.status_code == 200
    for field in ("title", "year", "description", "author"):
        assert field in response.data


@pytest.mark.django_db
def test_delete_book(client, set_up):
    book = Book.objects.first()
    response = client.delete(f"/books/{book.id}/", {}, format='json')
    assert response.status_code == 204
    books_ids = [book.id for book in Book.objects.all()]
    assert book.id not in books_ids


@pytest.mark.django_db
def test_update_book(client, set_up):
    book = Book.objects.first()
    response = client.get(f"/books/{book.id}/", {}, format='json')
    book_data = response.data
    new_year = 3
    book_data["year"] = new_year
    response = client.patch(f"/books/{book.id}/", book_data, format='json')
    assert response.status_code == 200
    book_obj = Book.objects.get(id=book.id)
    assert book_obj.year == new_year
