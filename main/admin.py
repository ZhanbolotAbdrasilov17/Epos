from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


admin.site.register(Statistic)
admin.site.register(Gallery)
admin.site.register(SocialMedia)
admin.site.register(ImagesContent)
admin.site.register(Employees)
admin.site.register(Lizer)
admin.site.register(Content)
admin.site.register(LizerCategory)
admin.site.register(Logo)

@admin.register(Mail)
class MailAdminList(admin.ModelAdmin):
    pass


@admin.register(ForAuthorCategory)
class ForAuthorCategoryAdminList(TranslationAdmin):
    pass

@admin.register(ForAuthor)
class ForAuthorAdminList(TranslationAdmin):
    pass

@admin.register(ForAuthorText)
class ForAuthorTextAdminList(TranslationAdmin):
    pass

@admin.register(Partner)
class PartnerAdminList(TranslationAdmin):
    pass

@admin.register(PartnerCategory)
class PartnerCategoryAdminList(TranslationAdmin):
    pass


@admin.register(Articles)
class ArticlesAdminList(TranslationAdmin):
    pass

@admin.register(ArticlesArchive)
class ArticlesArchiveAdminList(TranslationAdmin):
    pass

@admin.register(News)
class NewsAdminList(TranslationAdmin):
    pass

@admin.register(MainTagline)
class MainTaglineAdminList(TranslationAdmin):
    pass


@admin.register(NewsCircleTaglineOne)
class NewsCircleTaglineOneAdminList(TranslationAdmin):
    pass

@admin.register(NewsCircleTaglineTwo)
class NewsCircleTaglineTwoAdminList(TranslationAdmin):
    pass


@admin.register(BlueTagline)
class BlueTaglineAdminList(TranslationAdmin):
    pass

@admin.register(RedTagline)
class RedTaglineAdminList(TranslationAdmin):
    pass


@admin.register(AboutJournalCircleTagline)
class AboutJournalCircleTaglineAdminList(TranslationAdmin):
    pass

@admin.register(ArticlesTagline)
class ArticlesTaglineTaglineAdminList(TranslationAdmin):
    pass


@admin.register(NewsTagline)
class ArticlesTaglineTaglineAdminList(TranslationAdmin):
    pass

@admin.register(VideoContent)
class VideoContentTaglineAdminList(TranslationAdmin):
    pass

@admin.register(JournalsFiles)
class JournalsFilesTaglineAdminList(TranslationAdmin):
    pass

@admin.register(AboutJournalLowPart)
class AboutJournalLowPartTaglineAdminList(TranslationAdmin):
    pass


@admin.register(ArticlePage)
class ArticlePageTaglineAdminList(TranslationAdmin):
    pass


@admin.register(Contacts)
class ContactsAdminList(TranslationAdmin):
    pass
