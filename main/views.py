from django.conf.global_settings import EMAIL_HOST
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.conf import settings

from .forms import MailForm
from .models import *
from django.views.decorators.csrf import csrf_exempt


def home(request):
    partners = Partner.objects.all()
    category = PartnerCategory.objects.all()
    category_1 = PartnerCategory.objects.get(id=1)
    category_2 = PartnerCategory.objects.get(id=2)
    category_3 = PartnerCategory.objects.get(id=3)

    employees = Employees.objects.all()
    content = Content.objects.all()
    social_media = SocialMedia.objects.all()
    bluelines = BlueTagline.objects.all()
    redlines = RedTagline.objects.all()
    homepage_content_words = MainTagline.objects.all()
    logo = Logo.objects.get(id=1)

    context = {"partners":partners, 'category_1': category_1, 'category_2': category_2, 'category_3': category_3,
               'category':category, "content":content, "employees":employees, 'social_media': social_media,
               "bluelines":bluelines, "redlines":redlines, "homepage_content_words": homepage_content_words,
               "logo": logo, }
    return render(request, "home.html", context)


def appeal(request):
    if request.method == 'POST':
        data = request.POST
        msg = f'Файл {data["file"]} \n Имя {data["name"]}\n' \
              f' Текст {data["message"]} \n Почта {data["email"]} \n Телефон {data["phone"]}'
        send_mail('Образец', msg, settings.EMAIL_HOST_USER, ['zhanbolot19971997@gmail.com'])
    return HttpResponseRedirect(redirect_to=reverse('home'))


def about_journal(request):
    statistic_1 = Statistic.objects.get(id=4)
    statistic_2 = Statistic.objects.get(id=2)
    statistic_3 = Statistic.objects.get(id=3)

    low_part = AboutJournalLowPart.objects.all()
    circle_text = AboutJournalCircleTagline.objects.all()
    social_media = SocialMedia.objects.all()


    context = {"statistic_1": statistic_1, "statistic_2": statistic_2, "statistic_3": statistic_3,

               "low_part": low_part, "circle_text": circle_text, "social_media": social_media, }

    return render(request, "about_journal.html", context)


def contacts(request):
    social_media = SocialMedia.objects.all()
    context = {"social_media": social_media, }
    return render(request, "contacts.html", context )


def news(request):
    news = News.objects.all()
    social_media = SocialMedia.objects.all()
    video_content = VideoContent.objects.all()

    context = {"news": news, "social_media": social_media, "video_content": video_content, }
    return render(request, "news.html", context)

class NewsDetail(DetailView):
    model = News
    template_name = "news-detail.html"
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['social_media'] = SocialMedia.objects.all()
        return context


def article_releases(request):
    articles = Articles.objects.all()
    articles_archived = ArticlesArchive.objects.all()
    circle1 = NewsCircleTaglineOne.objects.all()
    circle2 = NewsCircleTaglineTwo.objects.all()
    gallery = ImagesContent.objects.all()
    social_media = SocialMedia.objects.all()
    circle_text = AboutJournalCircleTagline.objects.all()
    article_page = ArticlePage.objects.all()

    context = {"articles": articles, "articles_archived": articles_archived,
            "gallery": gallery, "circle1": circle1, "circle2": circle2, "social_media": social_media,
               "circle_text": circle_text, "article_page": article_page, }
    return render(request, "article_releases.html", context, )


class ArticleDetail(DetailView):
    model = Articles
    template_name = "article-releases-detail.html"
    context_object_name = 'articles'
    pk_url_kwarg = 'article_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['social_media'] = SocialMedia.objects.all()
        return context


class ArticleArchivedDetail(DetailView):
    model = ArticlesArchive
    template_name = "article-archived.html"
    context_object_name = 'articles_archived'
    pk_url_kwarg = 'article_archived_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['social_media'] = SocialMedia.objects.all()
        return context


def for_authors(request):
    title = ForAuthorText.objects.all()
    authors = ForAuthor.objects.get(id=1)
    category_authors = ForAuthorCategory.objects.all()
    category = ForAuthorCategory.objects.all()[1:]
    first_category = ForAuthorCategory.objects.all()[0]
    social_media = SocialMedia.objects.all()
    context = {"authors": authors, 'category': category, "title": title, 'first_category': first_category,
               'category_authors': category_authors, "social_media": social_media, }
    return render(request, "for_authors.html", context)


class MailCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST)

        if form.is_valid():
            form.save()
            last_sender = Mail.objects.first()
            message = f'Имя: {last_sender.name}\n' \
                      f'Почта: {last_sender.email}\n' \
                      f'Телефон: {last_sender.phone}\n' \
                      f'Текст: {last_sender.text}'

            send_mail(
                f'{last_sender.name} {last_sender.email}',
                message,
                'send_mail_asoi@mail.ru',
                ['itpythonzhanbolot@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('contacts'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')
