from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('article_releases/', article_releases, name='article_releases'),
    path('article/<int:article_id>/', ArticleDetail.as_view(), name='article'),
    path('for_authors/', for_authors, name='for_authors'),





]