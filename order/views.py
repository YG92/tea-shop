from django.http import HttpResponse
from .models import OrderItem
from django.views.generic import CreateView
from .forms import OrderCreateForm
from cart.cart import Cart

class OrderCreateView(CreateView):
    cart = Cart(request)
    form_class = OrderCreateForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            for item in self.cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            self.cart.clear()
            return HttpResponse('Спасибо за покупку')
        else:
            return self.form_invalid(form)
