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
    tagline = MainTagline.objects.all()[0]
    firstline = MainTagline.objects.all()[1]
    secondline = MainTagline.objects.all()[2]
    thirdline = MainTagline.objects.all()[3]
    employees = Employees.objects.all()
    content = Content.objects.all()
    social_media = SocialMedia.objects.all()
    bluelines = BlueTagline.objects.all()
    redlines = RedTagline.objects.all()

    context = {"partners":partners, 'category_1': category_1, 'category_2': category_2, 'category_3': category_3,
               'category':category, "content":content, "tagline":tagline, "firstline":firstline,
               "secondline":secondline, "thirdline":thirdline, "employees":employees, 'social_media': social_media,
               "bluelines":bluelines, "redlines":redlines,
               }
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
    fourthline = MainTagline.objects.all()[4]
    fifthline = MainTagline.objects.all()[5]
    sixthline = MainTagline.objects.all()[6]
    seventhline = MainTagline.objects.all()[7]
    eightline = MainTagline.objects.all()[8]
    nineteenthline = MainTagline.objects.all()[9]
    twentythline = MainTagline.objects.all()[10]
    twentyonethline = MainTagline.objects.all()[11]
    low_part = AboutJournalLowPart.objects.all()
    circle_text = AboutJournalCircleTagline.objects.all()

    context = {"statistic_1": statistic_1, "statistic_2": statistic_2, "statistic_3": statistic_3,
               "fourthline": fourthline, "fifthline": fifthline, "sixthline":sixthline,
               "seventhline":seventhline, "eightline":eightline, "nineteenthline": nineteenthline,
               "twentythline":twentythline, "twentyonethline": twentyonethline,
               "low_part": low_part, "circle_text": circle_text, }

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
        context['social_media'] = SocialMedia.objects.all()
        return context


def article_releases(request):
    articles = Articles.objects.all()
    articles_archived = ArticlesArchive.objects.all()
    number1 = MainTagline.objects.all()[22]
    number2 = MainTagline.objects.all()[23]
    number3 = MainTagline.objects.all()[24]
    number4 = MainTagline.objects.all()[25]
    text1 = MainTagline.objects.all()[26]
    text2 = MainTagline.objects.all()[27]
    circle1 = NewsCircleTaglineOne.objects.all()
    circle2 = NewsCircleTaglineTwo.objects.all()
    gallery = ImagesContent.objects.all()
    context = {"articles":articles, "articles_archived":articles_archived,
                "number1":number1, "number2":number2, "number3":number3, "number4":number4,
               "text1":text1, "text2":text2, "gallery":gallery, "circle1":circle1, "circle2":circle2,}
    return render(request, "article_releases.html", context )


class ArticleDetail(DetailView):
    model = Articles
    template_name = "article-releases-detail.html"
    context_object_name = 'articles'
    pk_url_kwarg = 'article_id'


class ArticleArchivedDetail(DetailView):
    model = ArticlesArchive
    template_name = "article-archived.html"
    context_object_name = 'articles_archived'
    pk_url_kwarg = 'article_archived_id'


def for_authors(request):
    title = ForAuthorText.objects.all()
    authors = ForAuthor.objects.get(id=1)
    category_authors = ForAuthorCategory.objects.all()
    category = ForAuthorCategory.objects.all()[1:]
    first_category = ForAuthorCategory.objects.all()[0]
    context = {"authors": authors, 'category': category, "title": title, 'first_category': first_category,
               'category_authors': category_authors}
    return render(request, "for_authors.html", context)


def article_article_releases(request):
    return render(request, "article-releases-detail.html", )


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
