import pytest


def test_smartphone_init(category_smartphone_1):
    assert category_smartphone_1.name == "Xiaomi Redmi Note 11"
    assert category_smartphone_1.description == "1024GB, Синий"
    assert category_smartphone_1.model == "15"
    assert category_smartphone_1.memory == 512
    assert category_smartphone_1.color == "Gray space"


def test_smartphone_add(category_smartphone_1, category_smartphone_2):
    assert category_smartphone_1 + category_smartphone_2 == 28


def test_smartphone_add_error(category_smartphone_1, category_lawngrass_1):
    with pytest.raises(TypeError):
        _ = category_smartphone_1 + category_lawngrass_1


def test_lawngrass_init(category_lawngrass_1):
    assert category_lawngrass_1.name == "Газонная трава"
    assert category_lawngrass_1.description == "Элитная трава для газона"
    assert category_lawngrass_1.price == 500.0
    assert category_lawngrass_1.quantity == 20
    assert category_lawngrass_1.country == "Россия"
    assert category_lawngrass_1.germination_period == "7 дней"
    assert category_lawngrass_1.color == "Зеленый"


def test_lawngrass_add(category_lawngrass_2, category_lawngrass_1):
    assert category_lawngrass_1 + category_lawngrass_2 == 35


def test_lawngrass_add_error(category_lawngrass_1, category_smartphone_1):
    with pytest.raises(TypeError):
        _ = category_lawngrass_1 + category_smartphone_1
