from . import views
from django.urls import path 


urlpatterns = [
    path("", views.new),
    path("book/", views.BookListView.as_view(), name ="book.all"),
    path('<int:id>', views.BookDetailView.as_view(), name= "book.show"),
    path('<int:id>/review', views.review, name="book.review")
]