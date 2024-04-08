from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete all no staff users'

    def handle(self, *args, **options):
        user = get_user_model()
        users = user.objects.filter(is_staff=False)
        if not users:
            print(f'No no staff users to delete')
            return
        users.delete()
        print(f'All no staff users deleted')
        return
