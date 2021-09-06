from . import views
from django.urls import path 


urlpatterns = [
    path("", views.new),
    path("book/", views.index, name ="book.all"),
    path('<int:id>', views.show, name= "book.show"),
    path('<int:id>/review', views.review, name="book.review")
]