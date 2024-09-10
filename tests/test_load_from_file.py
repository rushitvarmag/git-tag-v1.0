import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from main import load_from_file


@pytest.fixture
def sample_file_path():
    '''This fucntion returns a sample page number to test the download data function'''
    return 'test.json'

def test_load_from_file(sample_file_path):
    data = load_from_file(sample_file_path)
    assert data is not None
    


    


