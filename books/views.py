from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def book_list(request, format= None):
    if request.method=='GET':
        books=Book.objects.all()
        serializer= BookSerializer(books, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','Delete'])
def book_detail(request, id, format=None):
    try:
        book=Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=BookSerializer(book)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method =='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
