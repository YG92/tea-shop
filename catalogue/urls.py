from django.conf.urls import url
from .import views
from .views import ProductListView, AddProductsView

urlpatterns = [
url(r'^(?:(?P<cat>\d+)/)?$', ProductListView.as_view(), name='home'),
url(r'^add/', AddProductsView.as_view(), name='add-product'),
]
