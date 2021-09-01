from django.shortcuts import render
import json

# Create your views here.

booksData = open('books.json').read()

data = json.loads(booksData)

def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)

def show(request, id):
    singleBook = list()
    for book in data:
        if book['id'] == id:
            singleBook = book

    context = {'book': singleBook}
    return render(request, 'books/show.html', context)

def new(request):
    return render(request, 'books/new.html')
