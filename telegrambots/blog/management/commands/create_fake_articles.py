from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from blog.models import Article, Category, Tag

import random

from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = 'Create fake n articles'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        """Генерация аргументов для следующих полей:
        ○ заголовок статьи
        ○ содержание статьи
        ○ дата публикации статьи
        ○ автор статьи
        ○ категория статьи
        ○ теги статьи
        ○ количество просмотров статьи
        ○ флаг, указывающий, опубликована ли статья
        """
        user = get_user_model()
        authors = user.objects.filter(is_staff=False).all()
        if not authors:
            self.stdout.write(self.style.ERROR('No authors found.'))
            return
        categories = Category.objects.all()
        tags = Tag.objects.all()
        data = []
        for i in range(count):
            article = Article(
                title=f'Title{i}',
                description=lorem_ipsum.words(random.randint(1, 70)),
                content=f'Content{i}',
                author=random.choice(authors),
                category=random.choice(categories),
                views=random.randint(0, 100),
                is_published=random.choice([True, True, False])
            )
            data.append(article)
        Article.objects.bulk_create(data)
        if tags:
            for article in data:
                article.tags.set(random.sample(list(tags), random.randint(1, 5)))
                article.save()
        self.stdout.write(self.style.SUCCESS(f'Created {count} fake articles.'))
