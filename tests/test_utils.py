import json

from unittest.mock import patch, mock_open
from src.utils import read_json, created_objects_from_json
from tests.conftest import data_for_category


@patch('src.utils.open', new_callable=mock_open)
def test_read_json_file(mocked_open, data):
    json_string = json.dumps(data, ensure_ascii=False)
    mocked_open.return_value.read.return_value = json_string

    result = read_json('path.json')

    assert result == data


def test_created_objects_from_json(data_for_category):
    result = created_objects_from_json(data_for_category)
    category = result[0]

    assert category.name == "Смартфоны"
    assert category.products[0].name == "Samsung Galaxy C23 Ultra"
    assert category.products[1].name == "Iphone 15"
    assert category.products[2].name == "Xiaomi Redmi Note 11"