
class CatIterator:
    """Класс для перебора товара в одной категории"""
    def __init__(self, cat_obj):
        self.cat = cat_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.cat.product_in_list):
            prod = self.cat.product_in_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration
