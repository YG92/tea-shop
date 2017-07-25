from django.conf.urls import url
from .import views
from .views import ProductListView, AddProductsView

urlpatterns = [
url(r'^product/(?:(?P<cat>\d+)/)?$', ProductListView.as_view(), name='home'),
url(r'^product/add/', AddProductsView.as_view(), name='add-product'),
]
