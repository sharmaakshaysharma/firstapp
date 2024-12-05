from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)    

    def __str__(self):
        return self.name


class CoverType(models.Model):
    name = models.CharField(max_length=255,unique=True)    

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title =models.CharField(max_length=255,unique=True)
    author=models.CharField(max_length=255)
    description=models.TextField()
    isbn=models.CharField(max_length=255)
    price=models.FloatField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    coverType=models.ForeignKey(CoverType, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product_images/',null=True,blank=True)

    def __str__(self):
        return self.title


class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.title} - Views: {self.view_count}"