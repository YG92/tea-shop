from .cart import Cart
from catalogue.models import Product
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages


class CartDetailView(TemplateView):
    template_name = 'cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CartDetailView, self).get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        product = Product.objects.get(pk=product_id)
        if cart.quantity_valid(request, product, quantity):
            cart.update(product, quantity)
        else:
            messages.error(request, "Доступно всего %s" %(product.in_stock))
        return redirect ("/cart/")


def Remove(request, **kwargs):
    cart = Cart(request)
    product = get_object_or_404(Product, id=kwargs['id'])
    cart.remove(product)
    return redirect (request.META.get('HTTP_REFERER'))
