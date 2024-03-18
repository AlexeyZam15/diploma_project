from django.core.management.base import BaseCommand

from blog.models import Tag


class Command(BaseCommand):
    help = 'Create fake n tags'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        """Генерация аргументов для следующих полей:
        ○ Название тэга
        ○ Описание тэга
        """
        tags = Tag.objects.all()
        if tags:
            last_id = tags.order_by('-id')[0].id
        else:
            last_id = 1
        for i in range(count):
            Tag.objects.create(title=f'Tag{last_id + i}')

        self.stdout.write(self.style.SUCCESS(f'Created {count} fake tags'))
