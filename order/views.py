from django.shortcuts import redirect
from .models import OrderItem, Order
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderCreateForm
from cart.cart import Cart


class OrderCreateView(LoginRequiredMixin, FormView):
    form_class = OrderCreateForm
    template_name = 'create_order.html'
    login_url = '/account/login/'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context

    def get_initial(self):
        initial = super(OrderCreateView, self).get_initial()
        user = self.request.user
        initial["first_name"] = user.first_name
        initial["last_name"] = user.last_name
        return initial


    def form_valid(self, form):
        cart = Cart(self.request)
        if form.is_valid():
            form.instance.customer = self.request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return redirect('/thanks/')
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
