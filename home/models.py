from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    
    def __str__(self):
        return self.name

class ScrapedPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)  # E.g., "Amazon", "Flipkart"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.source}"
    
class PriceAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    desired_price = models.DecimalField(max_digits=10, decimal_places=2)

