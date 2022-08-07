from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html", )


def about(request):
    return render(request, "about.html", )

def news(request):
    return render(request, "news.html", )


def home(request):
    return render(request, "home.html", )

def article_releases(request):
    return render(request, "article_releases.html", )

def for_authors(request):
    return render(request, "for_authors.html", )
