from django.db import models
from django.contrib.auth.models import User
from store.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    is_checked_out = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'product')


    def __str__(self):
        return f"{self.product.title} in {self.user.username}'s cart"