from .cart import Cart
from .forms import CartAddProductForm
from catalogue.models import Product
from django.shortcuts import resolve_url, redirect, get_object_or_404
from django.views.generic import FormView, TemplateView


class CartAddFormView(FormView):
    form_class = CartAddProductForm
    template_name = 'cart_add.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        product = get_object_or_404(Product, id=kwargs['id'])
        if form.is_valid(request, **kwargs):
            form.cart_add(request, *args, **kwargs)
            return redirect ('/cart/')
        else:
            return self.form_invalid(form)


class CartDetailView(TemplateView):
    template_name = 'cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CartDetailView, self).get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context


def Remove(request, **kwargs):
    cart = Cart(request)
    product = get_object_or_404(Product, id=kwargs['id'])
    cart.remove(product)
    return redirect (request.META.get('HTTP_REFERER'))
