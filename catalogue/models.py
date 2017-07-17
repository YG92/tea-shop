from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="")
    rating = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
