import pytest
import pytz
from faker import Faker

from booksloans.models import Library, LoanBook
from books.settings import TIME_ZONE
from bookslist.models import Book
from .utils import fake_library_data


faker = Faker("pl_PL")
TZ = pytz.timezone(TIME_ZONE)


@pytest.mark.django_db
def test_add_library(client, set_up):
    library_count = Library.objects.count()
    new_library = fake_library_data()
    response = client.post("/libraries/", new_library, format='json')
    assert response.status_code == 201
    assert Library.objects.count() == library_count + 1
    for key, value in new_library.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_get_lib_list(client, library):
    response = client.get("/libraries/", {}, format='json')

    assert response.status_code == 200
    assert Library.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_library_detail(client, set_up):
    library = Library.objects.first()
    response = client.get(f"/libraries/{library.id}/", {}, format='json')

    assert response.status_code == 200
    for field in ("name", "city", "books"):
        assert field in response.data


@pytest.mark.django_db
def test_delete_library(client, set_up):
    library = Library.objects.first()
    response = client.delete(f"/libraries/{library.id}/", {}, format='json')
    assert response.status_code == 204
    libs_ids = [lib.id for lib in Library.objects.all()]
    assert library.id not in libs_ids


@pytest.mark.django_db
def test_update_library(client, set_up):
    library = Library.objects.first()
    response = client.get(f"/libraries/{library.id}/", {}, format='json')
    lib_data = response.data
    new_name = "DCF"
    lib_data["name"] = new_name
    response = client.patch(f"/libraries/{library.id}/", lib_data, format='json')
    assert response.status_code == 200
    lib_obj = Library.objects.get(id=library.id)
    assert lib_obj.name == new_name


@pytest.mark.django_db
def test_add_loan(client, set_up):
    loans_count = LoanBook.objects.count()
    new_loan_data = {
        "library": Library.objects.first().name,
        "book": Book.objects.first().title,
        "date": faker.date_time(tzinfo=TZ).isoformat()
        
    }
    response = client.post("/loans/", new_loan_data, format='json')
    assert response.status_code == 201
    assert LoanBook.objects.count() == loans_count + 1

    new_loan_data["date"] = new_loan_data["date"].replace('+00:00', 'Z')
    for key, value in new_loan_data.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_get_loaning_list(client, set_up):
    response = client.get("/loans/", {}, format='json')

    assert response.status_code == 200
    assert LoanBook.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_loaning_detail(client, set_up):
    loan = LoanBook.objects.first()
    response = client.get(f"/loans/{loan.id}/", {}, format='json')

    assert response.status_code == 200
    for field in ('book', 'library', 'date'):
        assert field in response.data


@pytest.mark.django_db
def test_delete_loan(client, set_up):
    loan = LoanBook.objects.first()
    response = client.delete(f"/loans/{loan.id}/", {}, format='json')
    assert response.status_code == 204
    loans_ids = [loan.id for loan in LoanBook.objects.all()]
    assert loan.id not in loans_ids


@pytest.mark.django_db
def test_update_loan(client, set_up):
    loan = LoanBook.objects.first()
    response = client.get(f"/loans/{loan.id}/", {}, format='json')
    loan_data = response.data
    new_library = Library.objects.last()
    loan_data["library"] = new_library.name
    response = client.patch(f"/loans/{loan.id}/", loan_data, format='json')
    assert response.status_code == 200
    loan_obj = LoanBook.objects.get(id=loan.id)
    assert loan_obj.library == new_library


