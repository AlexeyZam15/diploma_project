from django.contrib import admin, messages

import logging

from django.contrib.auth import get_user_model

from . import models

logger = logging.getLogger(__name__)


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email', 'bio', 'birth_date', 'date_joined', 'change_date')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_per_page = 15
    ordering = ('-change_date',)
    readonly_fields = ['date_joined', 'change_date']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_full_name', 'article_title', 'date_created', 'date_modified')
    search_fields = (
        'author__first_name', 'author__last_name', 'article__title', 'comment', 'date_created', 'date_modified')
    list_per_page = 15
    ordering = ('-date_modified',)
    readonly_fields = ['date_created', 'date_modified']
    list_filter = ('article', 'author')
    autocomplete_fields = ['author', 'article']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_full_name', 'category', 'is_published', 'date_published', 'change_date')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'category')
    list_per_page = 15
    ordering = ('-change_date',)
    readonly_fields = ['date_published', 'change_date']
    list_filter = ('author', 'is_published', 'category')
    autocomplete_fields = ['author', 'tags']
    actions = ['publish_articles', 'hide_articles']

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


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    list_per_page = 15
    ordering = ('id',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
    list_per_page = 15
    ordering = ('id',)
