from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from borrowing.models import Borrowing
from borrowing.serializers import BorrowingSerializer
import requests

DB_BOOK = requests.get("http://localhost:8000/books")
DB_CUSTOMER = requests("http://localhost:8000/customers")

@api_view(['GET', 'POST'])
def borrowing_list(request):
    """
    List all borrowing, or create a new borrowing.
    """
    if request.method == 'GET':
        borrowings = Borrowing.objects.all()
        serializer = BorrowingSerializer(borrowings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BorrowingSerializer(data=request.data)
        if serializer.is_valid() & DB_BOOK :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def borrowing_detail(request, pk):
    """
    Retrieve, update or delete a Borrowing.
    """
    try:
        borrowing = Borrowing.objects.get(pk=pk)
    except Borrowing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BorrowingSerializer(borrowing)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BorrowingSerializer(borrowing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        borrowing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)