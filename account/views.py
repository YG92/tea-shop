from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from .forms import UserForm
from django.contrib.auth import authenticate, login


class RegisterFormView(CreateView):
    form_class = UserForm
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
        login(self.request, new_user)
        return redirect('/order/profile/')
