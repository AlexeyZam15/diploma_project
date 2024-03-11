from django.core.management.base import BaseCommand

from blog.models import Article

import random

from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = 'Random change fake articles'

    def handle(self, *args, **options):
        articles = Article.objects.all()
        count = 0
        for article in articles:
            if random.randint(0, 2) != 0:
                continue
            count += 1
            article.desc = lorem_ipsum.words(random.randint(1, 70), common=False)
            article.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully changed {count} fake articles'))
        return
