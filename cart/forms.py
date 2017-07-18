from django import forms
from .cart import Cart
from catalogue.models import Product
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError


class CartAddProductForm(forms.Form):

    quantity = forms.IntegerField(initial=1,
                                min_value=1,
                                label='Количество:')


    def is_valid(self, request, **kwargs):
        valid = super(CartAddProductForm, self).is_valid()
        self.product = get_object_or_404(Product, id=kwargs['id'])
        self.cart = Cart(request)
        self.cd = self.cleaned_data
        if self.cart.not_valid(product=self.product, quantity=self.cd['quantity']):
            self.errors['Неверное количество:'] = '''
                        Всего доступно {} шт.'''.format(self.product.in_stock)
            return False
        return True

    def cart_add(self, request, **kwargs):
        self.cart.add(product=self.product, quantity=self.cd['quantity'])
