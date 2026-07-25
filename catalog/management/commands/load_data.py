from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загружает тестовые данные напрямую в базу'

    def handle(self, *args, **kwargs):
        self.stdout.write('Очистка базы данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Создание категорий...')
        cat1 = Category.objects.create(name="Электроника", description="Техника и гаджеты")
        cat2 = Category.objects.create(name="Книги", description="Художественная литература")
        cat3 = Category.objects.create(name="Одежда", description="Мужская и женская одежда")

        self.stdout.write('Создание продуктов...')
        Product.objects.create(name="Ноутбук", description="Игровой ноутбук", price=999.99, category=cat1)
        Product.objects.create(name="Смартфон", description="Флагманский смартфон", price=799.99, category=cat1)
        Product.objects.create(name="Наушники", description="Беспроводные наушники", price=149.99, category=cat1)
        Product.objects.create(name="Роман", description="Современный роман", price=19.99, category=cat2)
        Product.objects.create(name="Справочник", description="Справочник по Python", price=49.99, category=cat2)
        Product.objects.create(name="Футболка", description="Хлопковая футболка", price=29.99, category=cat3)
        Product.objects.create(name="Джинсы", description="Классические джинсы", price=79.99, category=cat3)

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))