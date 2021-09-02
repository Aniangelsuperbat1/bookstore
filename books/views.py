from django.shortcuts import render
from books.models import Book
from django.http import Http404
# Create your views here.


def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)

def show(request, id):
    try:
        singleBook = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        raise Http404('book not found')
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)

def new(request):
    return render(request, 'books/new.html')
