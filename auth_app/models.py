from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)   # Example field
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Example field
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp


    def __str__(self):
        return self.name