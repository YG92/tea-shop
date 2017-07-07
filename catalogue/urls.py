from django.conf.urls import url
from .import views
from .views import ProductListView, AddProductsView, ProductDetailView

urlpatterns = [
url(r'^(?:(?P<subcat>\d+)/)?$', ProductListView.as_view(), name='home'),
url(r'add-product', AddProductsView.as_view(), name='add-product'),
url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(),
    name='product_detail'),
]
