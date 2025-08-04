from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from book.forms import BookForm

# View to list all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'testapp/book_list.html', {'books': books})

# View to add or edit a book
def book_form(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list page
    else:
        form = BookForm(instance=book)
    
    return render(request, 'testapp/book_form.html', {'form': form, 'book': book})

# View to delete a book
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('book_list')  # Redirect to the book list page
