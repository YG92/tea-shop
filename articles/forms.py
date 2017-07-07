from django import forms
from .models import Article

class AddArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['added_at',]
        labels = {
        'title': ('Название статьи:'),
        'image': ('Загрузите изображение:'),
        'text': ('Текст статьи:'),
        }
