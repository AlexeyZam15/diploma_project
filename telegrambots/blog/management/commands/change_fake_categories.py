from django.core.management.base import BaseCommand

from blog.models import Category

from random import randint


class Command(BaseCommand):
    help = 'Change fake categories'

    def handle(self, *args, **options):
        categories = Category.objects.all()
        for category in categories:
            category.fake = randint(0, 1)
            category.save()
        self.stdout.write(self.style.SUCCESS('Fake categories changed'))
        return