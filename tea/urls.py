from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from catalogue.views import ProductListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^product/', include('catalogue.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^order/', include('order.urls', namespace='order')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
