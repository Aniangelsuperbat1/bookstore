from . import views
from django.urls import path 


urlpatterns = [
    path("book/", views.index),
    path('<int:id>', views.show)
]