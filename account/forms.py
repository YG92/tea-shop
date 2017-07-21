from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name',
                'last_name',
                'username')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
