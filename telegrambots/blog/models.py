from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    bio = models.TextField(verbose_name='Биография', null=True, blank=True)
    birth_date = models.DateField(verbose_name='День рождения', null=True, blank=True)
    change_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    fields = ['first_name', 'last_name', 'email', 'bio', 'birth_date']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} {self.email} {self.bio} {self.birth_date}'

    @property
    def articles(self):
        return Article.objects.filter(author=self)

    class Meta:
        ordering = ['-change_date']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = RichTextField(verbose_name='Описание', null=True, blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    @property
    def url_name(self):
        return "home"


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=25, verbose_name='Заголовок')
    description = models.TextField(max_length=255, verbose_name='Описание', null=True, blank=True)
    content = RichTextField(verbose_name='Содержание', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    change_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.FileField(upload_to='images/', verbose_name='Превью', null=True, blank=True)

    fields = ['title', 'content', 'category', 'views']

    @staticmethod
    def create_article(data):
        return Article.objects.create(**data)

    @staticmethod
    def get_articles():
        return Article.objects.all()

    @staticmethod
    def get_article(article_id):
        return Article.objects.filter(id=article_id).first()

    @staticmethod
    def update_article(article_id, field, value):
        article = Article.get_article(article_id)
        if article is None:
            return None
        setattr(article, field, value)
        article.save()
        return article

    @staticmethod
    def delete_article(article_id):
        article = Article.get_article(article_id)
        if article is None:
            return None
        article.delete()
        return article

    @property
    def comments(self):
        return Comment.objects.filter(article=self).all()

    def __str__(self):
        formatted_date = self.date_published.strftime('%d.%m.%Y %H:%M:%S')
        return f"{self.title} {self.content} {formatted_date} {self.author.full_name} {self.category} {self.views} {self.is_published}"

    class Meta:
        ordering = ['-change_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    @admin.display(description="Автор")
    def author_full_name(self):
        return self.author.full_name

    @staticmethod
    def get_published_posts():
        return Article.objects.filter(is_published=True).all()

    def changed(self):
        if self.date_published != self.change_date:
            return True
        return False


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                               verbose_name='Автор')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    comment = RichTextField(verbose_name='Комментарий', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    fields = ['comment']

    def __str__(self):
        format_date_create = self.date_created.strftime('%d.%m.%Y %H:%M:%S')
        format_date_mod = self.date_modified.strftime('%d.%m.%Y %H:%M:%S')
        return f"{self.author.full_name} {self.article.title} {self.comment} {format_date_create} {format_date_mod}"

    @staticmethod
    def get_comments(count=None, args=None, values=None):
        if args is not None and values is not None:
            data = Comment.objects.filter(args, values).all()
        else:
            data = Comment.objects.all()
        if count is not None:
            data = data[:count]
        return data

    def is_changed(self):
        """Сравнение даты создания и изменения без учёта секунд"""
        return self.date_created.strftime('%d.%m.%Y %H:%M') != self.date_modified.strftime('%d.%m.%Y %H:%M')

    class Meta:
        ordering = ['-date_modified']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    @admin.display(description='Автор')
    def author_full_name(self):
        return self.author.full_name

    @admin.display(description='Статья')
    def article_title(self):
        return self.article.title
