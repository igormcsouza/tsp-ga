from .types import RawData, Data


def data_to_list(raw_data: RawData) -> Data:
    new_data: Data = list()

    for each in raw_data:
        aux = each.split(" ")[1:]
        _tuple = (float(aux[0]), float(aux[1]))
        new_data.append(_tuple)

    return new_data

def take_header(raw_data: RawData, header_last_index: int) -> RawData:
    return raw_data[header_last_index:]
