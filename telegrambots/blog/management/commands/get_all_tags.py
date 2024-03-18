from django.core.management.base import BaseCommand

from blog.models import Tag


class Command(BaseCommand):
    help = 'Get all tags list'

    def handle(self, *args, **options):
        tags = Tag.objects.all()
        for tag in tags:
            self.stdout.write(tag.title)
        if not tags:
            self.stdout.write('No tags')
        return
