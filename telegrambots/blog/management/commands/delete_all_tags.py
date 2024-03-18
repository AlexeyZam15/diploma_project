from django.core.management.base import BaseCommand

from blog.models import Tag


class Command(BaseCommand):
    help = 'Delete all tags'

    def handle(self, *args, **options):
        Tag.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all categories'))
        return
