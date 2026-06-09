import pytest
from store_app.models import Product, Category


@pytest.mark.django_db
def test_product_creation(product):
    assert product.name == "Новый гаджет"
    assert product.description == "Новый гаджет в упаковке"
    assert product.price == 1000
    assert product.category.name == "Электроника"


@pytest.mark.django_db
def test_product_reading(product):
    retrieved_product = Product.objects.get(pk=product.pk)

    assert retrieved_product.name == product.name
    assert retrieved_product.description == product.description
    assert retrieved_product.price == product.price
    assert retrieved_product.category == product.category


@pytest.mark.django_db
def test_product_update(product):
    product.name = "Более новый гаджет"
    product.description = "Другая упаковка"
    product.price = 1100
    product.save()

    updated_product = Product.objects.get(pk=product.pk)

    assert updated_product.name == "Более новый гаджет"
    assert updated_product.description == "Другая упаковка"
    assert updated_product.price == 1100


@pytest.mark.django_db
def test_product_deletion(product):
    product_id = product.pk
    product.delete()

    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(pk=product_id)