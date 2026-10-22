from src.main import Product
from src.category_product import Smartphone, LawnGrass


def test_print_mixin(capsys):
    Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
