from rest_framework import serializers
from .models import Member, Author, Book, BorrowedBooks

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = '__all__'

    def validate(self, data):
        member = data.get('member')
        
        borrowed_count = BorrowedBooks.objects.filter(member=member, is_returned=False).count()
        
        if borrowed_count >= 5:
            raise serializers.ValidationError("Max Limit Reached")
        
        return data
