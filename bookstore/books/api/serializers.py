# Import serialier from Django Rest Framework
from rest_framework.serializers import ModelSerializer

from books.models import Book

# Create serializer to convert Book model into JSON
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
