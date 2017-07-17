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
        quantity = request.POST.get('quantity')
        in_stock = self.product.in_stock
        if int(quantity) <= in_stock:
            return True
        else:
            self.errors['Неверное количество:'] = '''
                        Всего доступно {} шт.'''.format(in_stock)
            return False


    def cart_add(self, request, **kwargs):
        cart = Cart(request)
        cd = self.cleaned_data
        cart.add(product=self.product, quantity=cd['quantity'])
