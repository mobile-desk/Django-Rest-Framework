from datetime import timezone

from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


    def get_date_since_published(self, obj):
        return (timezone.now().date() - obj.published_date.date()).days
