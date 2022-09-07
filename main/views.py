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

class NewsDetail(DetailView):
    model = Articles
    template_name = "news-detail.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context


def home(request):
    statistic_1 = Statistic.objects.get(id=1)
    statistic_2 = Statistic.objects.get(id=2)
    statistic_3 = Statistic.objects.get(id=3)
    partners = Partner.objects.all()
    category = PartnerCategory.objects.all()

    context = {"statistic_1":statistic_1, "statistic_2":statistic_2, "statistic_3":statistic_3, "partners":partners,
               "category":category}
    return render(request, "home.html", context)

def article_releases(request):
    articles = Articles.objects.all()
    articles_archived = ArticlesArchive.objects.all()
    context = {"articles":articles, "articles_archived":articles_archived}
    return render(request, "article_releases.html", context )

class ArticleDetail(DetailView):
    model = Articles
    template_name = "article-releases-detail.html"
    context_object_name = 'articles'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context

class ArticleArchivedDetail(DetailView):
    model = ArticlesArchive
    template_name = "article-archived.html"
    context_object_name = 'articles_archived'
    pk_url_kwarg = 'article_archived_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context

def for_authors(request):
    return render(request, "for_authors.html", )

def article_article_releases(request):
    return render(request, "article-releases-detail.html", )
