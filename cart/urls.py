from django.conf.urls import url
from .import views
from .views import CartDetailView

urlpatterns = [
url(r'^$', CartDetailView.as_view(), name='cart-detail'),
]
