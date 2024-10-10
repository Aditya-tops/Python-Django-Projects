from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg,Min

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"),Min("rating"))["rating__avg"]  # Fixed the aggregate syntax

    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_number_of_books': num_books,
        'average_rating': avg_rating
    })

def book_detail(request, slug):
    # Fetch book by slug using get_object_or_404 for safe error handling
    book = get_object_or_404(Book, slug=slug)
    
    # Pass book object directly to the template
    return render(request, "book_outlet/bookdetail.html", {
        "book": book
    })
