from django.conf import settings
from catalogue.models import Product
from django.contrib import messages


class Cart():

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def not_valid(self, product, quantity):
        in_stock = product.in_stock
        if int(quantity) > in_stock:
            return True
        return False


    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity,
                                     'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += quantity
        product.in_stock -= quantity
        product.save()
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            product.in_stock += self.cart[product_id]['quantity']
            product.save()
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids= self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
