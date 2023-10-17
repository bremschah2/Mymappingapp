from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='restaurant_photos/')
    # You can add more fields like ratings, opening hours, etc.
    
    def __str__(self):
        return self.name

class Rentalcars(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='rentalcars_photos/')
    # You can add more fields like ratings, opening hours, etc.
    
    def __str__(self):
        return self.name


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name}'
