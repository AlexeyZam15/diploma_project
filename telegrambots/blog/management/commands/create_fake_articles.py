from django.core.management.base import BaseCommand

from blog.models import Author
from blog.models import Article
from blog.models import Category

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
        ○ количество просмотров статьи
        ○ флаг, указывающий, опубликована ли статья
        """
        authors = Author.objects.all()
        categories = Category.objects.all()
        for i in range(count):
            data = {
                'title': f'Title{i}',
                'description': lorem_ipsum.words(random.randint(1, 70)),
                'content': f'Content{i}',
                'author': random.choice(authors),
                'category': random.choice(categories),
                'views': random.randint(0, 100),
                'is_published': random.choice([True, True, False])}
            Article.create_article(data)
        self.stdout.write(self.style.SUCCESS(f'Created {count} fake articles'))
