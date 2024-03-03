from django.core.management.base import BaseCommand

from blog.models import Category


class Command(BaseCommand):
    help = 'Delete all categories'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all categories'))
        return
