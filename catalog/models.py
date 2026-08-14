from django.db import models


class Category(models.Model):
    """
    Модель категории товаров
    Поля:
    - name: название категории
    - description: описание категории
    - created_at: дата создания записи в БД
    - updated_at: дата последнего изменения записи в БД
    """
    name = models.CharField(
        max_length=100,
        verbose_name="наименование"  # название поля в админке
    )
    description = models.TextField(
        blank=True,  # поле может быть пустым
        verbose_name="описание"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # автоматически заполняется при создании
        verbose_name="дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # автоматически обновляется при каждом сохранении
        verbose_name="дата последнего изменения"
    )

    class Meta:
        # Настройки отображения в админке
        verbose_name = "категория"          # в единственном числе
        verbose_name_plural = "категории"   # во множественном

    def __str__(self):
        """
        Возвращает название категории при выводе объекта
        Например: в админке, в shell, при выводе в консоль
        """
        return self.name


class Product(models.Model):
    """
    Модель продукта (товара)
    Поля:
    - name: название продукта
    - description: описание
    - image: изображение (опционально)
    - category: ссылка на категорию (ForeignKey)
    - price: цена
    - created_at: дата создания
    - updated_at: дата изменения
    - is_published:  поле «Опубликовано»
    - owner: поле владельца товара
    """
    name = models.CharField(
        max_length=100,
        verbose_name="наименование"
    )
    description = models.TextField(
        blank=True,
        verbose_name="описание"
    )
    image = models.ImageField(
        upload_to='products/',  # папка для загрузки картинок
        blank=True,  # может быть пустым
        null=True,   # может быть NULL в БД
        verbose_name="изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # при удалении категории удаляются все её продукты
        related_name='products',   # позволяет получить продукты категории через category.products
        verbose_name="категория"
    )
    price = models.DecimalField(
        max_digits=10,    # всего цифр: 1234567890
        decimal_places=2, # после запятой: 2 (копейки)
        verbose_name="цена за покупку"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="дата последнего изменения"
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
        ]

    def __str__(self):
        return self.name