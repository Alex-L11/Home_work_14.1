from src.cat_iterator import CatIterator


def test_cat_iterator(category_1):
    iterator = CatIterator(category_1)
    items = list(iterator)

    assert len(items) == 3
    assert items[0].name == 'Samsung Galaxy S23 Ultra'


def test_cat_iterator_empty_category(empty_category):
    iterator = CatIterator(empty_category)
    items = list(iterator)

    assert len(items) == 0