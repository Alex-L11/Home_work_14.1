import pytest

from src.main import Product

def test_product_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_category(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных " "функций для удобства жизни"
    assert category_1.category_count == 1
    assert category_1.product_count == 3


def test_products_property(category_1):
    assert category_1.products == ("Samsung Galaxy S23 Ultra, 180000 руб., Остаток: 5 шт.\n"
                                   "Iphone 15, 210000 руб., Остаток: 8 шт.\n"
                                   "Xiaomi Redmi Note 11, 31000 руб., Остаток: 14 шт.")

def test_add_product(category_1, data):
    initial_count = len(category_1._Category__products)

    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category_1.add_product(new_product)

    assert len(category_1._Category__products) == initial_count + 1
    assert category_1._Category__products[-1].name == 'Samsung Galaxy S23 Ultra'

def test_new_product(dict_for_test):
    data_1 = dict_for_test[0]
    data_2 = dict_for_test[1]
    data_3 = dict_for_test[2]
    product_1 = Product.new_product(data_1)
    product_2 = Product.new_product(data_2)
    product_3 = Product.new_product(data_3)

    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_2.name == "Iphone 15"
    assert product_2.quantity == 8
    assert product_3.price == 31000

def test_new_product_raises_name():
    with pytest.raises(ValueError, match="Поля 'name' и 'description' должны быть строчками."):
        Product.new_product({
            "name": 123,
            "description": None,
            "price": 100.0,
            "quantity": 3
            })

def test_new_product_raises_price():
    with pytest.raises(ValueError, match="Поля 'price' и 'quantity' должны иметь числовые типы."):
        Product.new_product({
            "name": "Test",
            "description": "test",
            "price": "100",
            "quantity": 3.5
            })

def test_new_product_update_quantity(dict_for_test):
    Product.new_product(dict_for_test[0])
    update_data = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 15
    }
    result = Product.new_product(update_data)

    assert result is Product.all_products[0]
    assert result.quantity == 20
    assert len(Product.all_products) == 1
