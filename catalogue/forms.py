from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['rating',]
        labels = {
        'subcategory': ('Выберите категорию:'),
        'name': ('Название товара:'),
        'image': ('Загрузите изображение:'),
        'price': ('Цена'),
        'description': ('Опишите товар:'),
        }
