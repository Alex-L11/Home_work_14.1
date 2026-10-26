from src.base_product import BaseEntity
from src.main import Product


class Smartphone(Product):
    """Класс для категорий товаров 'Смартфон'"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Product) -> int:
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        raise TypeError


class LawnGrass(Product):
    """Класс для категорий товара 'Трава газонная'"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Product) -> int:
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        raise TypeError


class Order(BaseEntity):
    """Класс в котором указано, какой товар был куплен, его стоимость и количество"""

    def __init__(self, name: str, description: str, product: Product, order_quantity: int) -> None:
        super().__init__(name, description)
        if order_quantity <= 0:
            raise ValueError('Количество в заказе должно быть положительным числом')

        self.product = product
        self.order_quantity = order_quantity
        self.total_price = self.product.price * self.order_quantity

    def __str__(self) -> str:
        return (
            f"{self.product.name} количество товара: {self.order_quantity}, цена за шт. {self.product.price}, "
            f"итоговая стоимость: {self.total_price}"
        )

    def info(self) -> str:
        return f'{self.name}, {self.description}, сумма заказа: {self.total_price}'
