from django.contrib import admin, messages

import logging

from . import models

logger = logging.getLogger(__name__)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'bio', 'birth_date', 'reg_date', 'change_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 15
    ordering = ('-change_date',)
    readonly_fields = ['reg_date', 'change_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_full_name', 'article_title', 'date_created', 'date_modified')
    search_fields = (
        'author__first_name', 'author__last_name', 'article__title', 'comment', 'date_created', 'date_modified')
    list_per_page = 15
    ordering = ('-date_modified',)
    readonly_fields = ['date_created', 'date_modified']
    list_filter = ('article', 'author')
    autocomplete_fields = ['author', 'article']


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author_full_name', 'category', 'views', 'is_published', 'date_published', 'change_date')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'category')
    list_per_page = 15
    ordering = ('-change_date',)
    readonly_fields = ['date_published', 'change_date']
    list_filter = ('author', 'is_published', 'category')
    autocomplete_fields = ['author']
    actions = ['publish_articles', 'hide_articles']
    list_display_links = ('id', 'title')

    @admin.action(description="Опубликовать статьи")
    def publish_articles(self, request, queryset):
        articles = queryset.filter(is_published=False)
        if not articles:
            messages.error(request, "Выберите скрытые статьи, которые хотите опубликовать")
            logger.error("Скрытые статьи не выбраны")
            return
        for article in articles:
            article.is_published = True
            article.save()
            logger.info(f"Статья {article.id} опубликована")
        messages.success(request, "Выбранные статьи опубликованы")

    @admin.action(description="Скрыть статьи")
    def hide_articles(self, request, queryset):
        articles = queryset.filter(is_published=True)
        if not articles:
            messages.error(request, "Выберите статьи, которые хотите скрыть")
            logger.error("Опубликованные статьи не выбраны")
            return
        for article in articles:
            article.is_published = False
            article.save()
            logger.info(f"Статья {article.id} скрыта")
        messages.success(request, "Выбранные статьи скрыты")


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
