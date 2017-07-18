from django.conf.urls import url
from .import views
from .views import OrderCreateView, ThanksView

urlpatterns = [
url(r'^create/$', OrderCreateView.as_view(), name='order'),
url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
]
