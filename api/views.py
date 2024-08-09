from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Member, Author, Book, BorrowedBooks
from .serializers import MemberSerializer, AuthorSerializer, BookSerializer, BorrowedBooksSerializer

@api_view(['GET'])
def retrieve_member(request, mem_id):
    try:
        member = Member.objects.get(pk=mem_id)
    except Member.DoesNotExist:
        return Response({'error': 'Member not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MemberSerializer(member)
    return Response(serializer.data)

@api_view(['POST'])
def add_member(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['POST'])
def add_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_borrowed_books(request, pk):
    try:
        borrowed_book = BorrowedBooks.objects.get(pk=pk)
    except BorrowedBooks.DoesNotExist:
        return Response({'error': 'Borrowed Book record not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BorrowedBooksSerializer(borrowed_book)
    return Response(serializer.data)

@api_view(['POST'])
def add_borrowed_books(request):
    serializer = BorrowedBooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
