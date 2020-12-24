import os
import shutil

from tsp_ga import dataset


def test_dataset_original_website():
    assert dataset.original_website().startswith('http://')

def test_dataset_download_data():
    # Prepare test
    if not os.path.exists('temp'): 
        os.mkdir('temp')

    # Execute the test
    dataset.download_data(path='temp')
    assert os.path.isfile('temp/usa115475.tsp') == True
    with open('temp/usa115475.tsp') as file:
        assert file.readline().rstrip() == 'NAME: usa115475'

    # Clean up the trash
    shutil.rmtree('temp')

def test_dataset_read_data():
    # Prepare test
    if not os.path.exists('temp'): 
        os.mkdir('temp')

    # Execute the test
    dataset.download_data(path='temp')
    data = dataset.read_data(path='temp')
    assert data[0].rstrip() == 'NAME: usa115475'

    # Clean up the trash
    shutil.rmtree('temp')

def test_dataset_read_data_full_path():
    # Prepare test
    if not os.path.exists('temp'): 
        os.mkdir('temp')

    # Execute the test
    data = dataset.read_data(path='data/usa115475.tsp')
    assert data[0].rstrip() == 'NAME: usa115475'

    # Clean up the trash
    shutil.rmtree('temp')

def test_dataset_preprocess_list_of_coordnates():
    pass

    

    