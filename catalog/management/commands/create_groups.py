from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" и назначает права'

    def handle(self, *args, **kwargs):
        # Получаем тип модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Получаем права
        unpublish_perm = Permission.objects.get(
            codename='can_unpublish_product',
            content_type=content_type,
        )
        delete_perm = Permission.objects.get(
            codename='delete_product',
            content_type=content_type,
        )

        # Создаём группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Назначаем права группе
        group.permissions.add(unpublish_perm, delete_perm)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана и права назначены'))