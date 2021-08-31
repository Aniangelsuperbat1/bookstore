from django.shortcuts import render
import json

# Create your views here.

booksData = open('\Users\ZhenP\OneDrive\Desktop\django_bookstore\books.json')

data = json.loads(booksData)

def index(request):
    context = {'data': data}
    return render(request, 'books/index.html', context)

