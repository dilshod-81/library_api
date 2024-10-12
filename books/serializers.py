from pyexpat import model
from unittest.mock import right
from django.contrib.auth import get_user_model
from django.template.defaultfilters import title
from rest_framework import serializers
from .models import Book
from  rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle','content', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise  ValidationError(
                {
                    'status': False,
                    'message': 'Kitob sarlavhasi faqat harflardan iborat bulishi kerak'
                }
            )
        if Book.objects.filter(title=title, author=author):
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kitob sarlavhasi va muallifi bir xil bulgan kitobni yuklab bulmaydi'
                }
            )
    def validate_price(self, price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )

class CashSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=150)
    output = serializers.CharField(max_length=150)


# DRF authentications
# authentications >> process >> login, logout, register

# basic authentications > username va password

# session authentications
   # username va password >>> basa >> sission ID > user
# token authentications

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')