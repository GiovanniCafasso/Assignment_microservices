from rest_framework import serializers
from borrowing.models import Borrowing

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ['id', 'id_customer', 'id_book']