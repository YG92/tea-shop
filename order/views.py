from django.shortcuts import redirect
from .models import OrderItem, Order
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderCreateForm
    template_name = 'create_order.html'
    login_url = '/account/login/'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        user = self.request.user
        form = self.form_class(request.POST, initial={
                                            'first_name': user.first_name,
                                            'last_name': user.last_name,
                                            'city': user.city,
                                            'address': user.address})
        if form.is_valid():
            form.instance.customer = user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return redirect('order:thanks')
        else:
            return self.form_invalid(form)


class OrderListView(ListView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order_list'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(customer=self.request.user.id)


class ThanksView(TemplateView):
    template_name = 'thanks.html'
