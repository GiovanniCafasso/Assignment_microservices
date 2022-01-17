from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from borrowing.models import Borrowing
from borrowing.serializers import BorrowingSerializer
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

import os
from kafka import KafkaProducer

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
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            DB_BOOK = session.get(urlBook)
            DB_CUSTOMER = session.get(urlCustomer)
            for customer in DB_CUSTOMER.json():
                if customer['id']==serializer.validated_data['id_customer']:
                    for book in DB_BOOK.json():
                        if book['id']==serializer.validated_data['id_book']: 
                            serializer.save()
                            # kafka
                            if os.getenv("POSITION") == "ConfigMap":    # kafka exists only in kubernetes environment
                                host = os.getenv("HOST_KAFKA")
                                port = os.getenv("PORT_KAFKA")
                                address = host + ':' + port
                                producer = KafkaProducer(bootstrap_servers=address)
                                producer.send('borrowing-notification', b'serializer.data')
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