# from django.test import TestCase    
from books.models import Book
from books.serializers import BookSerializer
from django.test import Client
from unittest import TestCase       # create a fake db

from django.test.client import RequestFactory
from books.views import book_detail

class BookTestCase(TestCase):

    def setUp(self):
    # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        print("Test details")
        # Create an instance of a GET request.
        request = self.factory.get('/books/1')

        # Test views.book_detail() as if it were deployed at /books
        Book.objects.create(id=10, title="views.book_detail()", author="views.book_detail()")        
        response = book_detail(request, 10)
        self.assertEqual(response.status_code, 200)
        print("*********************************************")

    # create 2 books and get all
    def test_post_plus_get(self):
        print("Test create 2 books and get all")
        Book.objects.create(title="title1", author="author1")
        Book.objects.create(title="title2", author="author2")
        print("Created books")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print("Serializer book: " + str(serializer.data))
        print("*********************************************")

    # Create book and update it
    def test_update(self):
        print("Test create book and update it")
        Book.objects.create(title="title1", author="author1")
        print("Created book")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print("Serializer book: " + str(serializer.data))
        Book.objects.update(title="title1", author="Mario")
        print("Updated book")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print("Serializer book: " + str(serializer.data))
        print("*********************************************")

    # test get 
    def test_get(self):
        print("Test get")
        Book.objects.create(title="titleA", author="authorA")
        Book.objects.create(title="titleB", author="authorB")
        c = Client()
        print("All books:")
        response = c.get('/books/')
        print(response.status_code)
        print(response.content)
        print("Book 1:")
        response = c.get('/books/1')
        print(response.status_code)
        print(response.content)
        print("*********************************************")