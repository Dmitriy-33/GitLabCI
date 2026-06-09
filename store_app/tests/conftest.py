import pytest
from store_app.models import Product, Category


@pytest.fixture
def category():
    return Category.objects.create(
        name="Электроника",
        description="Смартфоны, ноутбуки, гаджеты"
    )


@pytest.fixture
def product(category):
    return Product.objects.create(
        name='Новый гаджет',
        description='Новый гаджет в упаковке',
        price=1000,
        category=category
    )