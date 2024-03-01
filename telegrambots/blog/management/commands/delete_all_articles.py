from django.core.management.base import BaseCommand

from blog.models import Article


class Command(BaseCommand):
    help = 'Delete all articles'

    def handle(self, *args, **options):
        articles = Article.objects.all()
        if not articles:
            self.stdout.write(self.style.SUCCESS('No articles found'))
            return
        articles.delete()
        self.stdout.write(self.style.SUCCESS('All articles deleted'))
        return
