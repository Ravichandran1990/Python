from django.db import models

# Create your models here.

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

