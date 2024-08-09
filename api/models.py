from django.db import models

# Create your models here.

class Member(models.Model):
    mem_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    membership_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    
class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True, null=False)
    publication_year = models.IntegerField(null=False)
    copies_available = models.IntegerField(null=False)

    def __str__(self):
        return self.title
    
class BorrowedBooks(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        unique_together = ('member', 'book')

    def __str__(self):
        return f"{self.member.full_name} borrowed {self.book.title}"