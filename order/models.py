from django.db import models
from catalogue.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    customer = models.ForeignKey(User)

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def get_cost(self):
        return self.price * self.quantity
