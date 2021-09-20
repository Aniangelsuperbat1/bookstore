from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from books.form import ReviewForm
# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    # template_name = 'books/index.html'
    # context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all()


# def index(request):
#     dbData = Book.objects.all()
#     context = {'books': dbData}
#     return render(request, 'books/index.html', context)

class BookDetailView(DetailView):
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        context['form'] = ReviewForm()
        return context


# def show(request, id):
#     singleBook = get_object_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singleBook, 'reviews': reviews}
#     return render(request, 'books/show.html', context)


def author(request, author):
    books = Book.objects.filter(authors__name = author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)

def review(request, id):
    if request.user.is_authenticated:
        image = request.FILES['image']
        if image:
            fs = FileSystemStorage()
            name = fs.save(image.name, image)
            body = (request.POST['review'])
            newReview = Review(body=body, book_id = id, user=request.user)
            newReview.image=fs.url(name)
        newReview.save()
    return redirect('/book')





