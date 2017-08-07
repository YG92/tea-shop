from django.conf import settings
from catalogue.models import Product
from django.contrib import messages


class Cart():

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID) #получаем корзину
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {} #создаем, если нет
        self.cart = cart


#валидность количества товаров - нельзя добавить больше, чем есть на складе
    def quantity_valid(self, request, product, quantity):
        in_stock = product.in_stock
        if int(quantity) <= in_stock:
            return True
        return False

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart: #добавляем товар в корзину
            self.cart[product_id] = {'quantity': quantity,
                                     'price': str(product.price)}
        else: #обновляем кол-во, если товар уже в корзине
            self.cart[product_id]['quantity'] += quantity
        product.in_stock -= quantity
        product.save()
        self.save()

    def update(self, product, quantity): #обновляем кол-во
        quantity = int(quantity)
        product_id = str(product.id)
        self.cart[product_id]['quantity'] = quantity
        product.in_stock -= quantity
        product.save()
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product): #удаляем товар
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

    def get_total_quantity(self):  #общее кол-во товаров
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):  #общее кол-во товаров
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def empty(self):  #проверяем, пустая ли корзина
        if self.cart:
            return False
        return True
