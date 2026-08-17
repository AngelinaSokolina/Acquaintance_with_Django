from django.core.cache import cache
from .models import Product


def get_products_by_category(category_id):
    """
    Возвращает список продуктов в указанной категории.
    Данные кешируются в Redis на 10 минут.
    """
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        products = list(
            Product.objects.filter(category_id=category_id)
            .select_related('category')
        )
        cache.set(cache_key, products, 60 * 10)  # 10 минут

    return products