from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    city = forms.CharField(required=False)
    address = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name',
                'last_name',
                'city',
                'address')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.city = self.cleaned_data['city']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user
