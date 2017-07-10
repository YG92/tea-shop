from django.conf.urls import url
from .import views
from .views import CartAddFormView, CartDetailView

urlpatterns = [
url(r'^add/(?P<id>\d+)/$', CartAddFormView.as_view(), name='cart-add'),
url(r'^detail/', CartDetailView.as_view(), name='cart-detail'),
]
