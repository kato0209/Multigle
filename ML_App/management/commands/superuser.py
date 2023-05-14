from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from ../../../ML_Project import settings

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.SUPERUSER_NAME).exists():
            User.objects.create_superuser(
                username=settings.SUPERUSER_NAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD
            )
            print("スーパーユーザー作成")