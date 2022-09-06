from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
# Create your views here.


def about(request):
    return render(request, "about.html", )

def news(request):
    news = News.objects.all()
    context = {"news":news}
    return render(request, "news.html", context)


def home(request):
    return render(request, "home.html", )

def article_releases(request):
    articles = Articles.objects.all()
    context = {"articles":articles}
    return render(request, "article_releases.html", context )

class ArticleDetail(DetailView):
    model = Articles
    template_name = "article-releases-detail.html"
    context_object_name = 'articles'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context

def for_authors(request):
    return render(request, "for_authors.html", )

def article_article_releases(request):
    return render(request, "article-releases-detail.html", )
