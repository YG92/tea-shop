from django import forms
from .models import Order
from cart.cart import Cart


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name',
                'last_name',
                'city',
                'address']

        labels = {
                'first_name' : ('Фамилия'),
                'last_name': ('Имя'),
                'city': ('Город'),
                'address': ('Адрес')
        }
