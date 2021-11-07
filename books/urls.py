"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from booksloans.views import LibraryListView, LibraryView, LoanBookListView, LoanBookView
from bookslist.views import BookListView, BookView, AuthorListView, AuthorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookView.as_view(), name='book-detail'),
    path('libraries/', LibraryListView.as_view()),
    path('libraries/<int:pk>/', LibraryView.as_view(), name='library-detail'),
    path('loans/', LoanBookListView.as_view()),
    path('loans/<int:pk>/', LoanBookView.as_view()),
    path('authors/', AuthorListView.as_view()),
    path('authors/<int:pk>/', AuthorView.as_view()),

]
