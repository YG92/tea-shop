from django.shortcuts import redirect
from django.views.generic import FormView
from .forms import UserForm
from django.contrib.auth import authenticate, login


class RegisterFormView(FormView):
    form_class = UserForm
    template_name = 'register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(self.request, new_user)
            return redirect('/cart/')
        else:
            return self.form_invalid(form)
