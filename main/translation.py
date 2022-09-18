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


@register(ForAuthorText)
class ForAuthorTextTranslation(TranslationOptions):
    fields = ('title', )

@register(ForAuthor)
class ForAuthorTranslation(TranslationOptions):
    fields = ('title', 'text',)

@register(ForAuthorCategory)
class ForAuthorCategoryTranslation(TranslationOptions):
    fields = ('title', )


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
    fields = ('title1', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7', 'title8', 'title9', 'title10',)

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

@register(AboutJournalCircleTagline)
class AboutJournalTaglineTranslation(TranslationOptions):
    fields = ('title1', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7',  )

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
    fields = ('title', )

@register(JournalsFiles)
class JournalsFilesTranslation(TranslationOptions):
    fields = ('title', 'text', )


@register(AboutJournalLowPart)
class AboutJournalLowPartTranslation(TranslationOptions):
    fields = ('title', 'text', 'statistic_title', )


@register(ArticlePage)
class ArticlePageTranslation(TranslationOptions):
    fields = ('statistic_title', 'statistic_pre_title', 'statistic_text', 'button_blue', 'button_red', 'archived_title', )