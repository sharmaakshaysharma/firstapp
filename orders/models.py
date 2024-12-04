from django.db import models
from django.contrib.auth.models import User
from store.models import Product 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    STATUS_CHOICES = [
        ('processed', 'Processed'),
        ('shipped', 'Shipped'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processed')    
    # Timestamps for each status change
    processed_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    out_for_delivery_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"Order {self.id} by {self.user}"
    
    def update_status(self, status):
        """Updates the status of the order and its timestamp"""
        if status == 'processed' and not self.processed_at:
            self.status = 'processed'
            self.processed_at = models.DateTimeField(auto_now_add=True)
        elif status == 'shipped' and not self.shipped_at:
            self.status = 'shipped'
            self.shipped_at = models.DateTimeField(auto_now_add=True)
        elif status == 'out_for_delivery' and not self.out_for_delivery_at:
            self.status = 'out_for_delivery'
            self.out_for_delivery_at = models.DateTimeField(auto_now_add=True)
        elif status == 'delivered' and not self.delivered_at:
            self.status = 'delivered'
            self.delivered_at = models.DateTimeField(auto_now_add=True)        
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="address")
    name =models.CharField(max_length=255,null=True,blank=True)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.country}"
