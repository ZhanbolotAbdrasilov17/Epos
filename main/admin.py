from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


admin.site.register(Statistic)
admin.site.register(Articles)
admin.site.register(Categories)
admin.site.register(CategoriesForArchieved)
admin.site.register(ArticlesArchive)
admin.site.register(News)
admin.site.register(Partner)
admin.site.register(PartnerCategory)
admin.site.register(Gallery)
admin.site.register(SocialMedia)
admin.site.register(AuthorCategory)
admin.site.register(Authors)
admin.site.register(ImagesContent)
admin.site.register(MainTagline)
admin.site.register(Employees)
admin.site.register(Content)
admin.site.register(Lizer)
admin.site.register(LizerCategory)

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
