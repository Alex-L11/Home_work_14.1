import os
import json

from typing import cast
from src.main import Product, Category


def read_json(path: str) -> list[dict]:
    """Открывает JSON-файл"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    return cast(list[dict], data)


def created_objects_from_json(data: list[dict]) -> list:
    """ Создает список по категориям и товарам """
    products = []
    for prod in data:
        cats = []
        for cat in prod['products']:
            cats.append(Product(**cat))
        prod['products'] = cats
        products.append(Category(**prod))

    return products


if __name__ == '__main__':
    raw_data = read_json('../data/products.json')
    product_data = created_objects_from_json(raw_data)

    print(product_data[0].name)
    print(product_data[0].products)
