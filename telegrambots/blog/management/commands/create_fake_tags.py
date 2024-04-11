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
        ○ Слаг тэга
        """
        tags = Tag.objects.all()
        if tags:
            last_id = tags.order_by('-id')[0].id
        else:
            last_id = 1
        data = []
        for i in range(count):
            tag = Tag(title=f'Tag{last_id + i}', slug=f'tag{last_id + i}')
            data.append(tag)
        Tag.objects.bulk_create(data)
        self.stdout.write(self.style.SUCCESS(f'Created {count} fake tags'))
