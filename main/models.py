from django.db import models

# Create your models here.

class Statistic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статистики', blank=True, null=True)
    statistic = models.CharField(max_length=100, verbose_name='Статистика', blank=True, null=True)
    lower = models.CharField(max_length=100, verbose_name='Нижняя цифра', blank=True, null=True)
    comments = models.CharField(max_length=100, verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.id}  {self.title} '

    class Meta:
        verbose_name_plural = 'Главная - Статистика'
        verbose_name = 'Главная - Статистика'




class Categories(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'

class CategoriesForArchieved(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Категории для архивных статей'
        verbose_name = 'Категория для архивной статьи'



class ArticlesArchive(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    category_name = models.ForeignKey(CategoriesForArchieved, on_delete=models.CASCADE, related_name="Категории")
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    pdf = models.FileField()
    word = models.FileField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Архивные Статьи'
        verbose_name = 'Архивная Статья'

class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="Категории")
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    pdf = models.FileField()
    word = models.FileField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания новости')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'


class PartnerCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории партнёров'
        verbose_name = 'Кетегория партнёра'

class Partner(models.Model):
    category = models.ForeignKey(PartnerCategory, on_delete=models.CASCADE, verbose_name='Категория партнера',
                                 related_name='category_partners')
    title = models.CharField(max_length=200, verbose_name='Название партнёра')
    image = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Логотип партнера')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка на сайт партнера')

    def __str__(self):
        return self.title

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


class Authors(models.Model):
    title = models.CharField(max_length=200, verbose_name='Оглавление')
    text = models.TextField(verbose_name="Текст")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Для авторов'

class ImagesContent(models.Model):
    title = models.CharField(max_length=100, verbose_name="Картинка", blank=True, null=True)
    file = models.ImageField(null=True, blank=True, upload_to="work_images")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея_Контент'

class MainTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Главный слоган', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Слоганы в главной странице'
        verbose_name = 'Слоганы в главной странице'

class JournalTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Главный слоган', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Слоганы о журнале'
        verbose_name = 'Слоганы о журнале'


class NewsTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Главный слоган', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Слоганы в новостях'
        verbose_name = 'Слоганы о журнале'



class ArticlesTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Главный слоган', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Слоганы в вупусках'
        verbose_name = 'Слоганы в вупусках'




class FirstTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Первый слоган', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Первый слоган'
        verbose_name = 'Первый слоган'

class Employees(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

class Content(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="content")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Контенты'
        verbose_name = 'Контент'
        ordering = ['name']

class ContactLine(models.Model):
    title = models.CharField(max_length=200, verbose_name='Текст', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'