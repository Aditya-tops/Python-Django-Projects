from django.db import models

class Book(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    book_image = models.ImageField(default='default.jpg',upload_to='book_images/')