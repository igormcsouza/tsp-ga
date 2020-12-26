import os
from typing import Any, List

import requests

from .types import RawData, Data, Preprocessors


original_website = lambda : 'http://www.math.uwaterloo.ca/tsp/data/usa/index.html'

def download_data(path: str="/data") -> None:
    url = "http://www.math.uwaterloo.ca/tsp/data/usa/usa115475.tsp"

    response = requests.get(url=url, stream=True)

    with open(os.path.join(path, 'usa115475.tsp'), 'wb') as file:
        file.writelines(response.raw)

def read_data(path: str) -> RawData:
    if os.path.isdir(path):
        path = os.path.join(path, 'usa115475.tsp')

    with open(path, 'r') as file:
        data = file.readlines()

    return data

def preprocess_data(raw_data: RawData, preprocessors: Preprocessors) -> Data:
    # Apply Preprocessing
    change_list: List = list()
    change_list.append(raw_data)

    for preprocessor in preprocessors:
        change_list.append(preprocessor(change_list[-1]))

    assert type(change_list[-1]) == list, "Final preprocessor must return Type \
        Data"
    for each in change_list[-1]:
        assert type(each) == tuple, "Final preprocessor must return Type \
            Data"

    return change_list[-1]
