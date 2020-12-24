import re
import random

from tsp_ga.dataset import preprocessors


def test_dataset_preprocessors_data_to_list():
    data = [
        "1 33613.158800 86118.306100",
        "2 33100.954000 85529.675300",
        "3 31571.835200 85250.489300",
        "4 32070.429900 85687.725700",
        "5 33290.392600 87198.053000"
    ]

    result = preprocessors.data_to_list(data)

    assert type(result) == list
    index = random.randint(0, 4)
    assert result[index] == tuple([float(each) for each in data[index].split(" ")])[1:]

def test_dataset_preprocessors_take_header():
    data = [
        "Header -- Header"
        "1 33613.158800 86118.306100",
        "2 33100.954000 85529.675300",
        "3 31571.835200 85250.489300",
        "4 32070.429900 85687.725700",
        "5 33290.392600 87198.053000"
    ]

    result = preprocessors.take_header(
        raw_data=data,
        header_last_index=1
    )

    for each in result:
        assert re.match(r'(\d+\.*\d*)', each) != None
   