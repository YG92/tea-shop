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


    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context["articles"] = Article.objects.all().order_by('-added_at')
        return context


class AddArticleView(CreateView):
    form_class = AddArticleForm
    template_name = 'add_article.html'
    success_url = '/article/list/'
