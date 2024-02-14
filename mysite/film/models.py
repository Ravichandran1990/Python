from django.db import models

# Create your models here.

class Film(models.Model):
  filmname = models.CharField(max_length=255)
  
  def __str__(self):
    return self.filmname

class Actors(models.Model):
  actorsname = models.CharField(max_length=255)
  film = models.ForeignKey(Film, related_name="actors", on_delete=models.CASCADE)
  
  def __str__(self):
    return self.actorsname
  
class Product(models.Model):    
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default='Null')
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.name

class ProductStatus(models.Model):    
    name = models.CharField(max_length=100)    
    product = models.ForeignKey(Product, related_name="productstatus", on_delete=models.CASCADE)

    def __str__(self):
        return self.name