from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from borrowing.models import Borrowing
from borrowing.serializers import BorrowingSerializer
import requests

from pathlib import Path
import os
from dotenv import load_dotenv

# to manage environment variables
load_dotenv()
if os.getenv('POSITION') != "ConfigMap":
    dotenv_path = Path('microservices_borrowing/borrowing-config.env')
    load_dotenv(dotenv_path=dotenv_path)


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
        if serializer.is_valid():
            # checking if exist customer id and book id
            urlBook = "http://" + os.getenv("HOST_BOOK") + ":" + os.getenv("PORT_BOOK") + "/books/"  # create url to get all book
            urlCustomer = "http://" + os.getenv("HOST_CUSTOMER") + ":" + os.getenv("PORT_CUSTOMER") + "/customers/" # create url to get all customer
            DB_BOOK = requests.get(urlBook)
            DB_CUSTOMER = requests.get(urlCustomer)
            for customer in DB_CUSTOMER.json():
                if customer['id']==serializer.validated_data['id_customer']:
                    for book in DB_BOOK.json():
                        if book['id']==serializer.validated_data['id_book']: 
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                        else:
                            print("Book doesn't exist")
                else: 
                    print("Customer doesn't exist")                            
            print(serializer.data)
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