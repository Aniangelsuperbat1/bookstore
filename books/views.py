from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.views.generic import ListView
# Create your views here.

class BookListView(ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all()


# def index(request):
#     dbData = Book.objects.all()
#     context = {'books': dbData}
#     return render(request, 'books/index.html', context)

def show(request, id):
    singleBook = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book_id=id).order_by('-created_at')
    context = {'book': singleBook, 'reviews': reviews}
    return render(request, 'books/show.html', context)

def new(request):
    return render(request, 'books/new.html')

def review(request, id):
    body = (request.POST['review'])
    newReview = Review(body=body, book_id = id)
    newReview.save()
    return redirect('/book')

