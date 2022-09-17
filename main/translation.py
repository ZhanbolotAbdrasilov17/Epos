from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Statistic)
class StatisticTranslation(TranslationOptions):
    fields = ('title', 'comments',)

@register(Articles)
class ArticlesTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(ArticlesArchive)
class ArticlesTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(Authors)
class AuthorsTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(ImagesContent)
class ImageContentTranslation(TranslationOptions):
    fields = ('title',)

@register(PartnerCategory)
class PartnerCategoryTranslation(TranslationOptions):
    fields = ('title',)

@register(Partner)
class PartnerTranslation(TranslationOptions):
    fields = ('title',)

@register(MainTagline)
class MainTaglineTranslation(TranslationOptions):
    fields = ('title',)

@register(NewsCircleTaglineOne)
class NewsCircleTaglineOneTranslation(TranslationOptions):
    fields = ('title',)

@register(NewsCircleTaglineTwo)
class NewsCircleTaglineTwoTranslation(TranslationOptions):
    fields = ('title',)



@register(BlueTagline)
class BlueTaglineTranslation(TranslationOptions):
    fields = ('title',)


@register(RedTagline)
class RedTaglineTranslation(TranslationOptions):
    fields = ('title',)

@register(AboutJournalTagline)
class AboutJournalTaglineTranslation(TranslationOptions):
    fields = ('title',)

@register(ArticlesTagline)
class ArticlesTaglineTranslation(TranslationOptions):
    fields = ('title',)

@register(NewsTagline)
class NewsTaglineTranslation(TranslationOptions):
    fields = ('title',)


@register(Employees)
class EmployeesTranslation(TranslationOptions):
    fields = ('name', 'text')

@register(VideoContent)
class VideoContentTranslation(TranslationOptions):
    fields = ('title', 'video',)

@register(JournalsFiles)
class JournalsFilesTranslation(TranslationOptions):
    fields = ('title', 'text', )

@register(AuthorCategory)
class AuthorCategoryTranslation(TranslationOptions):
    fields = ('title', )

@register(AboutJournalLowPart)
class AboutJournalLowPartTranslation(TranslationOptions):
    fields = ('title', 'text', )