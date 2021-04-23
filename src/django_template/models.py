from django.db import models

# Create your models here.
class BookStore(models.Model):
    class Meta:
        verbose_name = "Book Store"
        verbose_name_plural = "Book Stores"
    book_title = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)
    year_published = models.CharField(max_length=4)
