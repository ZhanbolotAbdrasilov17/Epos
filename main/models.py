from django.db import models

# Create your models here.

class Statistic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статистики')
    statistic = models.CharField(max_length=100, verbose_name='Статистика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная - Статистика'
        verbose_name = 'Главная - Статистика'

class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    banner = models.ImageField(upload_to='project-banner', blank=True, null=True, verbose_name='Банер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'


class ArticlesArchive(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    banner = models.ImageField(upload_to='project-banner', blank=True, null=True, verbose_name='Банер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Архивные Статьи'
        verbose_name = 'Архивная Статья'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания новости')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')
    banner = models.ImageField(upload_to='project-banner', blank=True, null=True, verbose_name='Банер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'


class Partner(models.Model):
    image = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Логотип партнера')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка на сайт партнера')

    def __str__(self):
        return 'Онлайн журнал'

    class Meta:
        verbose_name_plural = 'Партнёры'
        verbose_name = 'Партнёр'


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя автора')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата жизни')
    image = models.ImageField(upload_to='gallery-images', verbose_name='Фото автора')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Галерея'
        verbose_name = 'Галерея'


class SocialMedia(models.Model):
    instagram = models.CharField(max_length=200, verbose_name='Инстаграм')
    telegram = models.CharField(max_length=200, verbose_name='Телеграм')
    facebook = models.CharField(max_length=200, verbose_name='Фейсбук')

    def __str__(self):
        return 'Социальные сети'

    class Meta:
        verbose_name_plural = 'Социальные_сети'
        verbose_name = 'Социальная_сеть'


class Partners(models.Model):
    partner_name = models.CharField(max_length=200, verbose_name="Название партнера")
    image = models.ImageField(upload_to='partners_images', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = 'Партнёры'