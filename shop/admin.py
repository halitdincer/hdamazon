from django.contrib import admin

from .models import Product,ProductImages,Category

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Category)

