from django.shortcuts import render
import json

# Create your views here.

booksData = open('books.json').read()

data = json.loads(booksData)

def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)

def show(request, id):
    context = {'books': data}
    return render(request, 'books/show.html', context)
