from django.conf.urls import url
from .import views
from .views import Remove, CartDetailView

urlpatterns = [
url(r'^remove/(?P<id>\d+)/$', views.Remove, name='cart-remove'),
url(r'^$', CartDetailView.as_view(), name='cart-detail'),
]
