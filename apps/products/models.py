from django.db import models
from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    country = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')

    def __str__(self):
        return f"{self.name}-{self.price}"

