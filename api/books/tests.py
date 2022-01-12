from django.test import TestCase    # create a fake db
from books.models import Book
from books.serializers import BookSerializer
from django.test import Client
# csrf_client = Client(enforce_csrf_checks=True)

class BookTestCase(TestCase):
    # create 2 books and get all
    def test_post_plus_get(self):
        Book.objects.create(title="title1", author="author1")
        Book.objects.create(title="title2", author="author2")
        print("Created books")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print("Serializer book: " + str(serializer.data))

    def test_update(self):
        Book.objects.create(title="title1", author="author1")
        print("Created book")
        Book.objects.update(title="title1", author="Mario")
        print("Updated book")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print("Serializer book: " + str(serializer.data))

    def test_get(self):
        Book.objects.create(title="title1", author="author1")
        c = Client()
        print("All books:")
        print(c.get('/books/'))
        print("Book 1:")
        print(c.get('/books/1'))
        # c.get('/books/details/', {'name': 'fred', 'age': 7})