from django.db import models
from ckeditor.fields import RichTextField


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True, null=True, verbose_name='Логотип')

    def __str__(self):
        return 'Логотип'

    class Meta:
        verbose_name_plural = 'Логотип'
        verbose_name = 'Логотип'


class Statistic(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статистики', blank=True, null=True)
    statistic = models.CharField(max_length=100, verbose_name='Статистика', blank=True, null=True)
    lower = models.CharField(max_length=100, verbose_name='Нижняя цифра', blank=True, null=True)
    comments = models.CharField(max_length=100, verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.id}.  {self.title}'

    class Meta:
        verbose_name_plural = 'О журнале - Статистика'
        verbose_name = 'О журнале - Статистика'


class ArticlesArchive(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = RichTextField(verbose_name="Текст", blank=True, null=True, )
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    pdf = models.FileField(blank=True, null=True,)
    word = models.FileField(blank=True, null=True,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Архивные Статьи'
        verbose_name = 'Архивная Статья'


class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания статьи')
    text = RichTextField(verbose_name="Текст", blank=True, null=True,)
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение')
    pdf = models.FileField(blank=True, null=True,)
    word = models.FileField(blank=True, null=True,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Выпуски - Статьи'
        verbose_name = 'Выпуски - Статьи'

class ArticlePage(models.Model):
    statistic_title = RichTextField(verbose_name='Заглавие статистики', blank=True, null=True)
    statistic_pre_title = models.CharField(max_length=200, verbose_name='Второе заглавие', blank=True, null=True)
    statistic_text = RichTextField(verbose_name='Текст статистики', blank=True, null=True)
    button_blue = models.CharField(max_length=200, verbose_name='Синяя кнопка', blank=True, null=True)
    button_red = models.CharField(max_length=200, verbose_name='Красная кнопка', blank=True, null=True)
    archived_title = models.CharField(max_length=200, verbose_name='Заголовок архива')
    number_blue1 = models.CharField(max_length=200, verbose_name='Цифры в синей статистики1', blank=True, null=True)
    number_blue2 = models.CharField(max_length=200, verbose_name='Цифры в синей статистики2', blank=True, null=True)
    number_red1 = models.CharField(max_length=200, verbose_name='Цифры в красной статистики1', blank=True, null=True)
    number_red2 = models.CharField(max_length=200, verbose_name='Цифры в красной статистики2', blank=True, null=True)

    def __str__(self):
        return 'Выпуске'

    class Meta:
        verbose_name_plural = 'Выпуски - страница'
        verbose_name = 'Выпуски - страница'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    date = models.CharField(max_length=200, blank=True, null=True, verbose_name='Дата создания новости')
    text = RichTextField(verbose_name='Текст', blank=True, null=True,)
    image = models.ImageField(upload_to='project-images', verbose_name='Изображение на показ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'


class JournalsFiles(models.Model):
    pdf = models.FileField(blank=True, null=True)
    word = models.FileField(blank=True, null=True)

    def __str__(self):
        return 'Файл руководства для авторов'

    class Meta:
        verbose_name_plural = 'Авторам - Документы'
        verbose_name = 'Авторам - Документы'


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




class SocialMedia(models.Model):
    instagram = models.CharField(max_length=200, verbose_name='Инстаграм')
    whatsapp = models.CharField(max_length=200, verbose_name='Ватсап')
    facebook = models.CharField(max_length=200, verbose_name='Фейсбук')

    def __str__(self):
        return 'Социальные сети'

    class Meta:
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'Социальная сеть'


class Partners(models.Model):
    partner_name = models.CharField(max_length=200, verbose_name="Название партнера")
    image = models.ImageField(upload_to='partners_images', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = 'Партнёры'


class ForAuthorCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Авторам - Категория'
        verbose_name_plural = 'Авторам - Категория'


class ForAuthor(models.Model):
    category = models.ForeignKey(ForAuthorCategory, on_delete=models.DO_NOTHING, verbose_name='Категория',
                                 related_name='author_category')
    title = models.CharField(max_length=200, verbose_name='Оглавление')
    text = RichTextField(verbose_name="Текст", blank=True, null=True)
    pdf = models.FileField(blank=True, null=True, upload_to='files')
    word = models.FileField(blank=True, null=True, upload_to='files')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Авторам - Описание'
        verbose_name_plural = 'Авторам - Описание'


class ForAuthorText(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Авторам - Заголовок'
        verbose_name_plural = 'Авторам - Заголовок'




class MainTagline(models.Model):
    title1 = models.CharField(max_length=200, verbose_name='Название главной страницы', blank=True, null=True)
    title2 = models.CharField(max_length=200, verbose_name='Предложение описание1', blank=True, null=True)
    title3 = models.CharField(max_length=200, verbose_name='Предложение описание2', blank=True, null=True)
    title4 = models.CharField(max_length=200, verbose_name='Manas1', blank=True, null=True)
    title5 = models.CharField(max_length=200, verbose_name='Epos1', blank=True, null=True)
    title6 = models.CharField(max_length=200, verbose_name='Manas2', blank=True, null=True)
    title7 = models.CharField(max_length=200, verbose_name='Manas2', blank=True, null=True)
    title8 = models.CharField(max_length=200, verbose_name='Название картинок', blank=True, null=True)
    title9 = models.CharField(max_length=200, verbose_name='Название афиши', blank=True, null=True)
    title10 = RichTextField(verbose_name='Название отправки сообщения', blank=True, null=True)

    def __str__(self):
        return "Главная страница контент"

    class Meta:
        verbose_name_plural = 'Главная - Контент'
        verbose_name = 'Главная - Контент'


class AboutJournalCircleTagline(models.Model):
    title1 = models.CharField(max_length=200, verbose_name='Текст1', blank=True, null=True)
    title2 = models.CharField(max_length=200, verbose_name='Текст2', blank=True, null=True)
    title3 = models.CharField(max_length=200, verbose_name='Текст3', blank=True, null=True)
    title4 = models.CharField(max_length=200, verbose_name='Текст4', blank=True, null=True)
    title5 = models.CharField(max_length=200, verbose_name='Текст5', blank=True, null=True)
    title6 = models.CharField(max_length=200, verbose_name='Текст6', blank=True, null=True)
    title7 = models.CharField(max_length=200, verbose_name='Текст7', blank=True, null=True)

    def __str__(self):
        return "Слова на планете странице о журнале"

    class Meta:
        verbose_name_plural = 'О журнале - планета'
        verbose_name = 'О журнале - планета'


class ArticlesCircleTagline(models.Model):
    title1 = models.CharField(max_length=200, verbose_name='Текст1', blank=True, null=True)
    title2 = models.CharField(max_length=200, verbose_name='Текст2', blank=True, null=True)
    title3 = models.CharField(max_length=200, verbose_name='Текст3', blank=True, null=True)
    title4 = models.CharField(max_length=200, verbose_name='Текст4', blank=True, null=True)
    title5 = models.CharField(max_length=200, verbose_name='Текст5', blank=True, null=True)
    title6 = models.CharField(max_length=200, verbose_name='Текст6', blank=True, null=True)
    title7 = models.CharField(max_length=200, verbose_name='Текст7', blank=True, null=True)

    def __str__(self):
        return "Слова на планете странице в выпусках"

    class Meta:
        verbose_name_plural = 'Выпуска - планета'
        verbose_name = 'Выпуска - планета'





class BlueTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Содержание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная - Эквалайзер - Синий'
        verbose_name = 'Главная - Эквалайзер - Синий'


class RedTagline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Содержание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная - Эквалайзер - Красный'
        verbose_name = 'Главная - Эквалайзер - Красный'


class NewsCircleTaglineOne(models.Model):
    title = models.CharField(max_length=200, verbose_name='Слово', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Выпуск - Круг1'
        verbose_name = 'Выпуск - Круг1'


class NewsCircleTaglineTwo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Слово', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Выпуск - Круг2'
        verbose_name = 'Выпуск - Круг2'


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
        verbose_name_plural = 'Мнение экспертов рынка'
        verbose_name = 'Мнение экспертов рынка'


class Content(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название картинки", blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="content")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name = 'Картинки'
        ordering = ['name']


class VideoContent(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название_видео", blank=True, null=True)
    video = models.CharField(max_length=100, verbose_name="Ссылка", blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="content")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости - Видео'
        verbose_name = 'Новости - Видео'



class AboutJournalLowPart(models.Model):
    title = models.CharField(max_length=200, verbose_name='Содержание', blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="content", verbose_name='Картинка')
    text = RichTextField(blank=True, null=True, verbose_name='Описание')
    statistic_title = RichTextField(verbose_name='Навзание поле статистики', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'О журнале'
        verbose_name = 'О журнале'


class Mail(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Обращения клиентов'
        verbose_name = 'Обращение клиентов'


class Contacts(models.Model):
    address = RichTextField(blank=True, null=True, verbose_name='Адресс')
    phone_number = RichTextField(blank=True, null=True, verbose_name='Номера')
    mail = RichTextField(blank=True, null=True, verbose_name='Почта')

    def __str__(self):
        return 'Полные контакты'

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'