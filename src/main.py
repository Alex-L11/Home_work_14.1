from typing import Optional


class Product:
    """Класс для продуктов"""
    name: str
    description: str

    all_products: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f'{self.name}, {round(self.__price)} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other: Product) -> int | float:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity
    # Метод, когда объект стоит справа

    def __radd__(self, other: int) -> int | float:
        if other == 0:
            return self.price * self.quantity
        return other + self.price * self.quantity

    @classmethod
    def new_product(cls, dict_products: dict) -> "Product":
        name = dict_products.get('name')
        description = dict_products.get('description')
        price = dict_products.get('price')
        quantity = dict_products.get('quantity')
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError("Поля 'name' и 'description' должны быть строчками.")
        if not isinstance(price, float) or not isinstance(quantity, int):
            raise ValueError("Поля 'price' и 'quantity' должны иметь числовые типы.")

        for prod in cls.all_products:
            if prod.name == name:
                prod.quantity += quantity
                prod.price = max(prod.price, price)
                return prod

        new_product = cls(name=name, description=description, price=price, quantity=quantity)
        cls.all_products.append(new_product)

        return new_product

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            output = input(
                f"Цена будет понижена с {round(self.__price)} до {round(value)}. Введите y(ДА)/n(НЕТ): "
            ).strip().lower()
            if output != 'y':
                print('Изменение цены отклонено.')
                return

        self.__price = value


class Category:
    """Класс для категорий товаров"""
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def __str__(self) -> str:
        prod_quantity = 0
        for prod in self.__products:
            prod_quantity += prod.quantity
        return f'{self.name}, количество продуктов: {prod_quantity} шт.'

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        output_str = ""
        for prod in self.__products:
            output_str += f"{str(prod)}\n"
        return output_str

    @property
    def product_in_list(self) -> list[Product]:
        return self.__products
