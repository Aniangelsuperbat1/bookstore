from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'book' : {
        'title': 'new book',
    }}
    return render(request, 'books/index.html', context)

