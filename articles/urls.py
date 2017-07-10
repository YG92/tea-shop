from django.conf.urls import url
from .import views
from .views import ArticleListView, ArticleDetailView, AddArticleView

urlpatterns = [
url(r'^detail/(?:(?P<pk>\d+)/)?$', ArticleDetailView.as_view(),
    name='article-detail'),
url(r'^list/$', ArticleListView.as_view(), name='article_list'),
url(r'^new/$', AddArticleView.as_view(), name='new_article'),
]
