from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Book
from .serializer import BookSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
