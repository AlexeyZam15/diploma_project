from django.core.management.base import BaseCommand

from blog.models import Category


class Command(BaseCommand):
    help = 'Get all categories list'

    def handle(self, *args, **options):
        categories = Category.objects.all()
        for category in categories:
            self.stdout.write(category.title)
        if not categories:
            self.stdout.write('No categories')
        return
