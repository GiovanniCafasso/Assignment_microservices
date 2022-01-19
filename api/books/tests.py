from django.test import TestCase    # create a fake db
from books.models import Book
from books.serializers import BookSerializer
from django.test import Client      

from rest_framework.test import APIRequestFactory
from books.views import book_detail

class BookTestCase(TestCase):

    def setUp(self):
    # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        Book.objects.create(id=1, title="title1", author="author1")
        Book.objects.create(id=2, title="title2", author="author2")
        Book.objects.create(id=5, title="title5", author="author5")
        Book.objects.create(id=10, title="title10", author="author10")

    def test_details_get(self):
        print("Test details get")
        # Create an instance of a GET request.
        request = self.factory.get('/books/5')

        # Test views.book_detail() as if it were deployed at /books        
        response = book_detail(request, 5)
        self.assertEqual(response.status_code, 200)
        print("*********************************************")

    def test_details_update(self):
        print("Test details update")
        # Create an instance of a PUT request.
        data = {'id': 1, 'author': 'Mario'}
        request = self.factory.put('/books/1', data)

        # Test views.book_detail() as if it were deployed at /books        
        response = book_detail(request, 1)
        self.assertEqual(response.status_code, 200)
        print(response)
        # verify update
        c = Client()
        print("All books:")
        response = c.get('/books/')
        print(response.status_code)
        print(response.content)
        print("*********************************************")

    # test get 
    def test_get(self):
        print("Test get")
        c = Client()
        print("All books:")
        response = c.get('/books/')
        print(response.status_code)
        print(response.content)
        print("Book 2:")
        response = c.get('/books/2')
        print(response.status_code)
        print(response.content)
        print("*********************************************")