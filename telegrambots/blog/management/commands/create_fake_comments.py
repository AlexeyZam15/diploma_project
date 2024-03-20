from django.core.management.base import BaseCommand

from blog.models import Author
from blog.models import Article
from blog.models import Comment

import random


class Command(BaseCommand):
    help = 'Create fake n articles'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        """Генерация аргументов для следующих полей:
        ○ автор
        ○ статья
        ○ комментарий
        """
        authors = [author for author in Author.objects.all()]
        articles = [article for article in Article.objects.all()]
        data = []
        for i in range(count):
            comment = Comment(
                author=random.choice(authors),
                article=random.choice(articles),
                comment=f'Comment_{i}'
            )
            data.append(comment)
        Comment.objects.bulk_create(data)
        self.stdout.write(self.style.SUCCESS(f'{count} fake comments created!'))
