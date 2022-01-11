from django.test import TestCase    # create a fake db
from books.models import Book
from books.serializers import BookSerializer

class BookTestCase(TestCase):
    # post 2 books into fake db and get all data
    def test_post_plus_get(self):
        Book.objects.create(title="title1", author="author1")
        Book.objects.create(title="title2", author="author2")
        print("Created book")
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        print("Serializer book: " + str(serializer.data))

