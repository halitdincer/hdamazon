from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    main_image = models.ImageField(upload_to="product_images/%Y/%m/%d")
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/%Y/%m/%d")

    

