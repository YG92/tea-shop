from django.conf.urls import url
from .import views
from .views import RegisterFormView
from django.contrib.auth.views import login, logout


urlpatterns = [
url(r'^register/$', RegisterFormView.as_view(), name='register'),
url(r'^login/', login, {'template_name': 'login.html'}, name='login'),
url(r'^logout/', logout, name='logout'),]
