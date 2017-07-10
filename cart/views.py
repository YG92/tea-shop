from .cart import Cart
from .forms import CartAddProductForm
from catalogue.models import Product
from django.shortcuts import resolve_url, redirect, get_object_or_404
from django.views.generic import FormView, TemplateView, UpdateView

class CartAddFormView(TemplateView):
    form_class = CartAddProductForm
    template_name = 'cart_add.html'
    success_url = '/product/'
    product = None


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        cart = Cart(request)
        product = get_object_or_404(Product, id=kwargs['id'])
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'],
                    update_quantity=cd['update'])
            return redirect ('home')
        else:
            return super(CartAddFormView, self).get(request, *args, **kwargs)


class CartDetailView(FormView):
    form_class = CartAddProductForm
    template_name = 'cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CartDetailView, self).get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context

    def form_valid(self, form):
        return super(CartDetailFormView, self).form_valid(form)
