from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = 'Create fake n users'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='Number of users to create')

    def handle(self, *args, **options):
        user = get_user_model()
        if user.objects.count() == 0:
            last_id = 1
        else:
            last_id = user.objects.last().id + 1
        count = options['n']
        data = [user(
            username=f'user{last_id + i}',
            password='qwertyuasd',
            email=f'user{last_id + i}@example.com',
            first_name=f'user{last_id + i}',
            last_name=f'user{last_id + i}', )
            for i in range(count)]
        user.objects.bulk_create(data)
        self.stdout.write(self.style.SUCCESS(f'{count} fake users created'))
        return
