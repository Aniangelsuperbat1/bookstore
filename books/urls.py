from . import views
from django.urls import path 


urlpatterns = [
    path("", views.new),
    path("book/", views.index),
    path('<int:id>', views.show)
]