from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('catalogue.urls')),
    url(r'', include('articles.urls')),
    url(r'^login/', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout, name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
