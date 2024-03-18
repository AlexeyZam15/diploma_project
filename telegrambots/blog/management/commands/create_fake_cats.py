from django.core.management.base import BaseCommand

from blog.models import Category

import random


class Command(BaseCommand):
    help = 'Create fake n categories'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        """Генерация аргументов для следующих полей:
        ○ Название категории
        """
        categories = Category.objects.all()
        if categories:
            last_id = categories.order_by('-id')[0].id
        else:
            last_id = 1
        for i in range(count):
            Category.objects.create(title=f'Category{last_id + i}', description=f'Description{last_id + i}')

        self.stdout.write(self.style.SUCCESS(f'Created {count} fake categories'))
