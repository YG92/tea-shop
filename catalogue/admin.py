from django.contrib import admin
from .models import Product, Category, Subcategory

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)