from django.shortcuts import render, resolve_url
from .models import Article
from django.views.generic import ListView, CreateView, DetailView
from .forms import AddArticleForm

class ArticleDetailView(DetailView):

    model = Article
    template_name = 'article_detail.html'


class ArticleListView(ListView):

    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

    def get_queryset(self, **kwargs):
        queryset = super(ArticleListView, self).get_queryset()
        return queryset.order_by('-added_at')


class AddArticleView(CreateView):
    form_class = AddArticleForm
    template_name = 'add_article.html'
    success_url = '/article/list/'
