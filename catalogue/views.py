from django.shortcuts import render, resolve_url, redirect
from django.forms.models import modelformset_factory
from .models import Product, Category, Subcategory
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .forms import AddProductForm
from cart.forms import CartAddProductForm
from cart.cart import Cart


class ProductDetailView(DetailView):

    model = Product
    template_name = 'product_detail.html'
    subcat = None

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.all()
        context["subcategory"] = self.subcat
        context["form"] = CartAddProductForm
        context["cart"] = Cart(self.request)
        return context


class ProductListView(ListView):

    model = Product
    template_name = 'home.html'
    subcat = None

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.all()
        context["subcategory"] = self.subcat
        context["cart"] = Cart(self.request)
        return context

    def get(self, request, *args, **kwargs):
        if self.kwargs["subcat"]:
            self.subcat = Subcategory.objects.get(pk=self.kwargs["subcat"])
        return super(ProductListView, self).get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.sort_field = request.GET.get('sort_field')
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.kwargs["subcat"] == None:
            queryset = Product.objects.all()
        else:
            queryset = Product.objects.filter(subcategory=self.subcat)
        if self.sort_field:
            queryset = queryset.order_by(self.sort_field)
        return queryset

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        cart.add(product)
        return redirect('home')


class AddProductsView(CreateView):
    form_class = AddProductForm
    template_name = 'add_product.html'
    success_url = '/product/'
