from django.shortcuts import redirect
from .models import Product, Category
from django.views.generic import ListView, CreateView
from .forms import AddProductForm
from cart.cart import Cart


class ProductListView(ListView):

    model = Product
    template_name = 'home.html'
    cat = None

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.all()
        context["category"] = self.cat
        context["cart"] = Cart(self.request)
        return context

    def get(self, request, *args, **kwargs):
        if self.kwargs["cat"]:
            self.cat = Category.objects.get(pk=self.kwargs["cat"])
        return super(ProductListView, self).get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.sort_field = request.GET.get('sort_field')
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.kwargs["cat"] == None:
            queryset = Product.objects.filter(category=1)
        else:
            queryset = Product.objects.filter(category=self.cat)
        if self.sort_field:
            queryset = queryset.order_by(self.sort_field)
        return queryset

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        quantity = 1
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        cart.add(product, quantity)
        return redirect (request.META.get('HTTP_REFERER'))


class AddProductsView(CreateView):
    form_class = AddProductForm
    template_name = 'add_product.html'
    success_url = '/'
