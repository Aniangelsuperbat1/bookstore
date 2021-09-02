from django.shortcuts import render, get_object_or_404
from books.models import Book
# Create your views here.


def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)

def show(request, id):
    
    singleBook = Book.objects.get(pk=id)
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)

def new(request):
    return render(request, 'books/new.html')
