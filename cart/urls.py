from django.conf.urls import url
from .import views
from .views import Remove, CartAddFormView, CartDetailView#, CartRemoveView

urlpatterns = [
url(r'^add/(?P<id>\d+)/$', CartAddFormView.as_view(), name='cart-add'),
url(r'^remove/(?P<id>\d+)/$', views.Remove, name='cart-remove'),
url(r'^$', CartDetailView.as_view(), name='cart-detail'),
]
