from src.main import Product


class Smartphone(Product):
    """ Класс для категорий товаров 'Смартфон' """
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
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
    """ Класс для категорий товара 'Трава газонная' """
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Product) -> int:
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        raise TypeError
