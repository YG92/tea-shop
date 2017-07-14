from django.conf.urls import url
from .import views
from .views import OrderCreateView

urlpatterns = [
url(r'^create/$', OrderCreateView.as_view(), name='order'),
]
