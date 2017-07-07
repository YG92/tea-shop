from django.shortcuts import render, resolve_url, redirect
from django.forms.models import modelformset_factory
from .models import Product, Category, Subcategory
from articles.models import Article
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .forms import AddProductForm


class ProductDetailView(DetailView):

    model = Product
    template_name = 'product_detail.html'
    subcat = None

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.all()
        context["articles"] = Article.objects.all().order_by('-added_at')[0:3]
        context["subcategory"] = self.subcat
        return context


class ProductListView(ListView):

    model = Product
    template_name = 'home.html'
    subcat = None

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.all()
        context["subcategory"] = self.subcat
        context["articles"] = Article.objects.all().order_by('-added_at')[0:3]
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


ProductFormSet = modelformset_factory(Product,
can_delete = True,
exclude=('rating', 'available',),
labels = {
'subcategory': ('Выберите категорию:'),
'name': ('Название товара:'),
'image': ('Загрузите изображение:'),
'price': ('Цена:'),
'description': ('Опишите товар:'),
'in_stock': ('Количество:'),
},
max_num=10,
extra=5)


class AddProductsView(TemplateView):

    formset = None
    template_name = 'add_product.html'

    def get(self, request, *args, **kwargs):
        self.formset = ProductFormSet()
        return super(AddProductsView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AddProductsView, self).get_context_data(**kwargs)
        context["formset"] = self.formset
        return context

    def post(self, request, *args, **kwargs):
        self.formset = ProductFormSet(request.POST, request.FILES)
        if self.formset.is_valid():
            self.formset.save()
            return redirect ('home')
        else:
            return super(AddProductsView, self).get(request, *args, **kwargs)
