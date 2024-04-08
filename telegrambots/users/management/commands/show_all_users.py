from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Show all no staff users'

    def handle(self, *args, **options):
        user = get_user_model()
        users = user.objects.filter(is_staff=False)
        for user in users:
            print(user)
        print(f'Total: {len(users)}')
        return
