import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from main import download_data


@pytest.fixture
def sample_page_no():
    '''This fucntion returns a sample page number to test the download data function'''
    return 20

def test_download_data(sample_page_no):
    data = download_data(sample_page_no)
    assert data is not None
    assert 'page' in data
    


    


