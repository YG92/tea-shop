from django.shortcuts import redirect
from .models import OrderItem
from django.views.generic import CreateView
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderCreateView(CreateView):
    form_class = OrderCreateForm
    template_name = 'create_order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = self.form_class(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return redirect('home')
        else:
            return self.form_invalid(form)
