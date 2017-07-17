from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class RegisterFormView(CreateView):
    form_class = UserCreationForm
    success_url = '/account/login/'
    template_name = 'register.html'
