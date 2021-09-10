from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=255)
class Book(models.Model):
    title = models.CharField(max_length=200)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=200, null=True)
    shortDescription = models.CharField(max_length=200, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(Authors)

    def __str__(self):
        return f'{self.id} {self.title}'

class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)


