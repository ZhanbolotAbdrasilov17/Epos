from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
# Create your views here.


def about_journal(request):
    statistic_1 = Statistic.objects.get(id=4)
    statistic_2 = Statistic.objects.get(id=2)
    statistic_3 = Statistic.objects.get(id=3)
    context = {"statistic_1": statistic_1, "statistic_2": statistic_2, "statistic_3": statistic_3,}

    return render(request, "about_journal.html", context)

def contacts(request):
    return render(request, "contacts.html", )

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

    partners = Partner.objects.all()
    category = PartnerCategory.objects.all()
    category_1 = PartnerCategory.objects.get(id=1)
    category_2 = PartnerCategory.objects.get(id=2)
    category_3 = PartnerCategory.objects.get(id=3)


    context = {"partners":partners, 'category_1': category_1, 'category_2': category_2, 'category_3': category_3,
               'category':category}
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
    authors = Authors.objects.all()
    context = {"authors": authors}
    return render(request, "for_authors.html", context )

def article_article_releases(request):
    return render(request, "article-releases-detail.html", )
